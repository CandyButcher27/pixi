import json
import random
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
INSPO = ROOT / "research/harvest/Nutlope__inspo"
SCREENS = INSPO / "screens"
RATINGS = ROOT / "research/ratings/ratings.jsonl"
MIN_QUALITY = 70
CHOICES = {"left", "right", "tie", "both_generic", "skip"}

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>pixi rating</title>
<style>
body{margin:0;font:14px system-ui;background:#111;color:#ddd}
header{padding:10px 16px;display:flex;gap:24px;align-items:center}
main{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:0 8px}
figure{margin:0;cursor:pointer;border:3px solid transparent}
figure:hover{border-color:#e0b04a}
img{width:100%;display:block}
figcaption{padding:4px 2px;color:#999}
kbd{background:#333;padding:1px 6px;border-radius:3px}
</style></head><body>
<header><b id="type"></b><span id="count"></span>
<span><kbd>&larr;</kbd> left <kbd>&rarr;</kbd> right <kbd>&darr;</kbd> tie <kbd>g</kbd> both generic <kbd>s</kbd> skip</span></header>
<main><figure id="left"><img><figcaption></figcaption></figure><figure id="right"><img><figcaption></figcaption></figure></main>
<script>
let pair;
async function next(){
  pair = await (await fetch('/pair')).json();
  document.getElementById('type').textContent = 'Which is better designed? (' + pair.page_type + ')';
  document.getElementById('count').textContent = pair.done + ' rated';
  for (const side of ['left','right']) {
    const f = document.getElementById(side);
    f.querySelector('img').src = '/img/' + pair[side] + '/hero.png';
    f.querySelector('figcaption').textContent = pair[side];
  }
  window.scrollTo(0,0);
}
async function rate(choice){
  await fetch('/rate', {method:'POST', body: JSON.stringify({...pair, choice})});
  next();
}
document.getElementById('left').onclick = () => rate('left');
document.getElementById('right').onclick = () => rate('right');
document.onkeydown = e => {
  const k = {ArrowLeft:'left', ArrowRight:'right', ArrowDown:'tie', g:'both_generic', s:'skip'}[e.key];
  if (k) { e.preventDefault(); rate(k); }
};
next();
</script></body></html>"""


def load_pool() -> dict[str, list[str]]:
    rows = json.loads((INSPO / "packages/db/src/static-screens.json").read_text(encoding="utf-8"))
    pool: dict[str, list[str]] = {}
    for r in rows:
        if int(r.get("qualityScore") or 0) >= MIN_QUALITY and (SCREENS / r["slug"] / "hero.png").exists():
            pool.setdefault(r.get("pageType") or "other", []).append(r["slug"])
    return {t: s for t, s in pool.items() if len(s) >= 2}


def rated_pairs() -> set[frozenset[str]]:
    if not RATINGS.exists():
        return set()
    lines = RATINGS.read_text(encoding="utf-8").splitlines()
    return {frozenset((r["left"], r["right"])) for r in map(json.loads, lines)}


def pick_pair(pool: dict[str, list[str]], seen: set[frozenset[str]], rng: random.Random) -> tuple[str, str, str]:
    types = list(pool)
    weights = [len(pool[t]) for t in types]
    for _ in range(1000):
        page_type = rng.choices(types, weights)[0]
        left, right = rng.sample(pool[page_type], 2)
        if frozenset((left, right)) not in seen:
            return page_type, left, right
    raise RuntimeError("no unrated pairs left")


class Handler(BaseHTTPRequestHandler):
    pool: dict[str, list[str]] = {}
    seen: set[frozenset[str]] = set()
    rng = random.Random()

    def send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/":
            return self.send(200, PAGE.encode(), "text/html; charset=utf-8")
        if path == "/pair":
            page_type, left, right = pick_pair(self.pool, self.seen, self.rng)
            body = {"page_type": page_type, "left": left, "right": right, "done": len(self.seen)}
            return self.send(200, json.dumps(body).encode(), "application/json")
        if path.startswith("/img/"):
            slug, name = path[5:].split("/", 1)
            file = (SCREENS / slug / name).resolve()
            if file.is_relative_to(SCREENS.resolve()) and file.is_file():
                return self.send(200, file.read_bytes(), "image/png")
        self.send(404, b"not found", "text/plain")

    def do_POST(self) -> None:
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if data.get("choice") not in CHOICES or not all(isinstance(data.get(k), str) for k in ("left", "right", "page_type")):
            return self.send(400, b"bad rating", "text/plain")
        row = {k: data[k] for k in ("page_type", "left", "right", "choice")} | {"ts": time.time(), "source": "inspo"}
        RATINGS.parent.mkdir(parents=True, exist_ok=True)
        with RATINGS.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
        self.seen.add(frozenset((row["left"], row["right"])))
        self.send(204, b"", "text/plain")

    def log_message(self, *args) -> None:
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    Handler.pool, Handler.seen = load_pool(), rated_pairs()
    print(f"{sum(map(len, Handler.pool.values()))} sites in {len(Handler.pool)} page types; open http://127.0.0.1:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
