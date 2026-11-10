import json
import random
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BLIND = ROOT / "builds/blind"
BRIEFS = json.loads((BLIND / "briefs.json").read_text(encoding="utf-8"))
RATINGS = BLIND / "ratings.jsonl"
ARMS = ("control", "treatment")
CHOICES = {"left", "right", "tie", "both_generic"}

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>blind rating</title>
<style>
body{margin:0;font:14px system-ui;background:#111;color:#ddd}
header{position:sticky;top:0;z-index:1;background:#111;padding:10px 16px;display:flex;gap:24px;align-items:center;border-bottom:1px solid #333}
main{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:8px}
img{width:100%;display:block;border:3px solid transparent;cursor:pointer}
img:hover{border-color:#e0b04a}
kbd{background:#333;padding:1px 6px;border-radius:3px}
</style></head><body>
<header><b id="brief"></b><span id="count"></span>
<span><kbd>&larr;</kbd> left <kbd>&rarr;</kbd> right <kbd>&darr;</kbd> tie <kbd>g</kbd> both generic</span></header>
<main><img id="left"><img id="right"></main>
<script>
let pair;
async function next(){
  pair = await (await fetch('/pair')).json();
  if (pair.finished) { document.body.innerHTML = '<h2 style="padding:24px">All ' + pair.done + ' pairs rated.</h2>'; return; }
  document.getElementById('brief').textContent = 'Which is the better landing page for: ' + pair.brief;
  document.getElementById('count').textContent = (pair.done + 1) + ' / ' + pair.total;
  for (const side of ['left','right']) document.getElementById(side).src = '/img/' + pair.slug + '/' + pair.token + '/' + side;
  window.scrollTo(0,0);
}
async function rate(choice){ await fetch('/rate', {method:'POST', body: JSON.stringify({token: pair.token, choice})}); next(); }
document.getElementById('left').onclick = () => rate('left');
document.getElementById('right').onclick = () => rate('right');
document.onkeydown = e => {
  const k = {ArrowLeft:'left', ArrowRight:'right', ArrowDown:'tie', g:'both_generic'}[e.key];
  if (k) { e.preventDefault(); rate(k); }
};
next();
</script></body></html>"""


STARS = BLIND / "standouts.json"

GALLERY = """<!doctype html><html><head><meta charset="utf-8"><title>standouts</title>
<style>
body{margin:0;font:14px system-ui;background:#111;color:#ddd}
header{position:sticky;top:0;z-index:2;background:#111;padding:10px 16px;border-bottom:1px solid #333}
main{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;padding:12px}
figure{margin:0;border:3px solid transparent;cursor:pointer;position:relative}
figure.on{border-color:#e0b04a}
figure img{width:100%;height:340px;object-fit:cover;object-position:top;display:block}
figcaption{padding:4px;color:#999}
#view{display:none;position:fixed;inset:0;z-index:3;background:#000d;overflow:auto}
#view img{width:min(1100px,96vw);display:block;margin:56px auto}
#bar{position:fixed;top:0;left:0;right:0;padding:10px 16px;background:#111;display:flex;gap:16px;z-index:4}
button{font:inherit;padding:6px 14px;cursor:pointer}
</style></head><body>
<header>Click a page to open it full size. Star the ones that stand out. <span id="n"></span></header>
<main id="grid"></main>
<div id="view"><div id="bar"><button id="star"></button><button id="close">close (Esc)</button><span id="brief"></span></div><img id="big"></div>
<script>
let items=[], cur=null;
const n=()=>document.getElementById('n').textContent=items.filter(i=>i.starred).length+' starred';
function paint(i){i.el.classList.toggle('on',i.starred);}
function open(i){cur=i;document.getElementById('big').src='/gimg/'+i.id;document.getElementById('brief').textContent=i.brief;
  document.getElementById('star').textContent=i.starred?'★ starred':'☆ star';document.getElementById('view').style.display='block';document.getElementById('view').scrollTop=0;}
async function toggle(){cur.starred=!cur.starred;await fetch('/star',{method:'POST',body:JSON.stringify({id:cur.id,starred:cur.starred})});
  paint(cur);n();document.getElementById('star').textContent=cur.starred?'★ starred':'☆ star';}
document.getElementById('star').onclick=toggle;
document.getElementById('close').onclick=()=>document.getElementById('view').style.display='none';
document.onkeydown=e=>{if(e.key==='Escape')document.getElementById('view').style.display='none';if(e.key==='s'&&cur&&document.getElementById('view').style.display==='block')toggle();};
(async()=>{items=await(await fetch('/items')).json();const g=document.getElementById('grid');
  items.forEach((i,k)=>{const f=document.createElement('figure');f.innerHTML='<img loading="lazy" src="/gimg/'+i.id+'"><figcaption>#'+(k+1)+' · '+i.brief+'</figcaption>';
  f.onclick=()=>open(i);i.el=f;paint(i);g.appendChild(f);});n();})();
</script></body></html>"""


def shoot() -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for page_file in sorted(BLIND.glob("*/*/index.html")):
            slug, arm = page_file.parent.parent.name, page_file.parent.name
            shot = page_file.with_name("screenshot.png")
            if shot.exists():
                continue
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(page_file.as_uri(), wait_until="load")
            page.wait_for_timeout(1500)
            page.screenshot(path=str(shot), full_page=True)
            page.close()
            print(f"shot {slug}/{arm}")
        browser.close()


def rated() -> set[str]:
    if not RATINGS.exists():
        return set()
    return {r["slug"] for r in map(json.loads, RATINGS.read_text(encoding="utf-8").splitlines())}


def ready() -> list[str]:
    return [s for s in BRIEFS if all((BLIND / s / a / "screenshot.png").exists() for a in ARMS)]


def tally(rows: list[dict]) -> dict[str, int]:
    out = {a: 0 for a in ARMS} | {"tie": 0, "both_generic": 0}
    for r in rows:
        out[r[r["choice"]] if r["choice"] in ("left", "right") else r["choice"]] += 1
    return out


def load_stars() -> dict[str, bool]:
    return json.loads(STARS.read_text(encoding="utf-8")) if STARS.exists() else {}


class Handler(BaseHTTPRequestHandler):
    pending: dict[str, dict] = {}
    gallery: dict[str, str] = {}

    def send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/":
            return self.send(200, PAGE.encode(), "text/html; charset=utf-8")
        if path == "/pair":
            todo = [s for s in ready() if s not in rated()]
            if not todo:
                return self.send(200, json.dumps({"finished": True, "done": len(rated())}).encode(), "application/json")
            slug = random.choice(todo)
            left, right = random.sample(ARMS, 2)
            token = f"{random.getrandbits(64):016x}"
            self.pending[token] = {"slug": slug, "left": left, "right": right}
            body = {"slug": slug, "token": token, "brief": BRIEFS[slug], "done": len(rated()), "total": len(ready())}
            return self.send(200, json.dumps(body).encode(), "application/json")
        if path == "/gallery":
            return self.send(200, GALLERY.encode(), "text/html; charset=utf-8")
        if path == "/items":
            stars = load_stars()
            items = [{"id": gid, "brief": BRIEFS[key.split("/")[0]], "starred": stars.get(key, False)}
                     for gid, key in self.gallery.items()]
            return self.send(200, json.dumps(items).encode(), "application/json")
        if path.startswith("/gimg/") and path[6:] in self.gallery:
            return self.send(200, (BLIND / self.gallery[path[6:]] / "screenshot.png").read_bytes(), "image/png")
        parts = path.split("/")
        if len(parts) == 5 and parts[1] == "img" and parts[3] in self.pending and parts[4] in ("left", "right"):
            pair = self.pending[parts[3]]
            shot = BLIND / pair["slug"] / pair[parts[4]] / "screenshot.png"
            return self.send(200, shot.read_bytes(), "image/png")
        self.send(404, b"not found", "text/plain")

    def do_POST(self) -> None:
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if urlparse(self.path).path == "/star":
            key = self.gallery.get(data.get("id"))
            if key is None:
                return self.send(400, b"bad id", "text/plain")
            stars = load_stars() | {key: bool(data.get("starred"))}
            STARS.write_text(json.dumps(stars, indent=2), encoding="utf-8")
            return self.send(204, b"", "text/plain")
        pair = self.pending.pop(data.get("token"), None)
        if pair is None or data.get("choice") not in CHOICES:
            return self.send(400, b"bad rating", "text/plain")
        row = pair | {"choice": data["choice"], "ts": time.time()}
        with RATINGS.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
        self.send(204, b"", "text/plain")

    def log_message(self, *args) -> None:
        pass


def main() -> None:
    global ARMS, RATINGS
    cmd = sys.argv[1] if len(sys.argv) > 1 else "serve"
    if len(sys.argv) == 4:
        ARMS = (sys.argv[2], sys.argv[3])
        RATINGS = BLIND / f"ratings_{ARMS[0]}_{ARMS[1]}.jsonl"
    if cmd == "shoot":
        shoot()
    elif cmd == "summary":
        rows = list(map(json.loads, RATINGS.read_text(encoding="utf-8").splitlines())) if RATINGS.exists() else []
        print(f"{len(rows)} rated: {tally(rows)}")
    elif cmd == "standouts":
        picked = sorted(k for k, v in load_stars().items() if v)
        by_arm = {a: [k.split("/")[0] for k in picked if k.endswith("/" + a)] for a in ARMS}
        print(f"{len(picked)} starred: " + ", ".join(f"{a} {len(v)} {v}" for a, v in by_arm.items()))
    else:
        keys = [f"{s}/{a}" for s in ready() for a in ARMS]
        random.shuffle(keys)
        Handler.gallery = {f"{random.getrandbits(64):016x}": k for k in keys}
        print(f"{len(ready())} pairs ready, {len(rated())} rated; open http://127.0.0.1:8766  (standouts: /gallery)")
        ThreadingHTTPServer(("127.0.0.1", 8766), Handler).serve_forever()


if __name__ == "__main__":
    main()
