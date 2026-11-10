"""Pick screenshot references for a brief, outside the recurring Claude house style.

  uv run python scripts/pick_reference.py "<brief>" [-n 5]

Looks in the local gallery harvest first. When fewer than n topical candidates exist, it asks
scrappy (Agents/scraping-agent) to search the web, then visits the found sites itself with
Playwright after a robots.txt check, and adds them to the harvest. Prints JSON candidates,
best first; the caller still has to look at each screenshot before using it.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib import robotparser
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from designmcp.catalogue import tokens  # noqa: E402
from measure_live import OUT, SHOTS, SITES, measure_chunk  # noqa: E402

SCRAPPY = ROOT.parent / "scraping-agent"
UA = "pixi-reference-bot"
HOUSE_FONTS = ("fraunces", "plex", "mono", "newsreader", "gloock")


def slug(url: str) -> str:
    return url.split("//", 1)[-1].strip("/").replace("/", "_")[:120]


def house_traits(metrics: dict) -> list[str]:
    fam = (metrics.get("display_font_family") or "").lower()
    out = [f for f in HOUSE_FONTS if f in fam]
    if "serif" in fam and "sans" not in fam:
        out.append("serif display")
    rgb = [float(x) for x in re.findall(r"[\d.]+", (metrics.get("backgrounds") or [""])[0])[:3]]
    if len(rgb) == 3 and rgb[0] >= rgb[1] >= rgb[2] and sum(rgb) / 3 > 215 and rgb[0] - rgb[2] >= 6:
        out.append("warm paper background")
    return out


def load_sites() -> dict[str, dict]:
    if not SITES.exists():
        return {}
    return {s["url"]: s for s in map(json.loads, SITES.read_text(encoding="utf-8").splitlines())}


def candidates(brief: str, sites: dict[str, dict]) -> list[dict]:
    if not OUT.exists():
        return []
    q = set(tokens(brief))
    out = []
    for row in map(json.loads, OUT.read_text(encoding="utf-8").splitlines()):
        shot = SHOTS / f"{slug(row['url'])}.png"
        if "grammar" not in row or not shot.exists() or shot.stat().st_size < 40_000:
            continue
        if house_traits(row["metrics"]):
            continue
        meta = sites.get(row["url"], {})
        text = " ".join([row["url"], *meta.get("titles", []), *(t.split(":", 1)[-1] for t in meta.get("tags", []))])
        tiebreak = hashlib.sha1(f"{brief}|{row['url']}".encode()).hexdigest()
        out.append({"url": row["url"], "screenshot": str(shot), "relevance": len(q & set(tokens(text))),
                    "imagery": row["grammar"].get("imagery"), "_tie": tiebreak})
    out.sort(key=lambda c: (-c["relevance"], c["_tie"]))
    return out


def allowed(url: str) -> bool:
    rp = robotparser.RobotFileParser(f"{urlparse(url).scheme}://{urlparse(url).netloc}/robots.txt")
    try:
        rp.read()
    except Exception:
        return True
    return rp.can_fetch(UA, url)


def scrappy_search(brief: str, n: int) -> list[str]:
    cmd = ["uv", "run", "scrappy", "search", f"{brief} website", "-n", str(n)]
    res = subprocess.run(cmd, cwd=SCRAPPY, capture_output=True, text=True, encoding="utf-8", timeout=180)
    try:
        urls = [r["url"] for r in json.loads(res.stdout).get("results", [])]
        return [u for u in urls if urlparse(u).path in ("", "/")]
    except (json.JSONDecodeError, AttributeError):
        print(f"scrappy search failed: {res.stderr[-300:]}", file=sys.stderr)
        return []


def fetch_new(brief: str, sites: dict[str, dict], limit: int) -> int:
    q = set(tokens(brief))
    done = {json.loads(line)["url"] for line in OUT.read_text(encoding="utf-8").splitlines()} if OUT.exists() else set()
    listed = [u for u, s in sites.items() if u not in done
              and q & set(tokens(" ".join([u, *s.get("titles", []), *s.get("tags", [])])))]
    urls = listed[:limit] if listed else []
    if len(urls) < limit and SCRAPPY.exists():
        urls += [u for u in scrappy_search(brief, limit * 2) if u not in done][: limit - len(urls)]
    urls = [u for u in urls if allowed(u)]
    if not urls:
        return 0
    rows = measure_chunk(urls)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("a", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row) + "\n")
    return sum("grammar" in r for r in rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("brief")
    ap.add_argument("-n", type=int, default=5)
    args = ap.parse_args()
    sites = load_sites()
    found = candidates(args.brief, sites)
    if sum(c["relevance"] > 0 for c in found) < args.n:
        print(f"scrappy: fetched {fetch_new(args.brief, sites, args.n * 2)} new references", file=sys.stderr)
        found = candidates(args.brief, sites)
    for c in found:
        c.pop("_tie")
    print(json.dumps(found[: args.n], indent=2))


if __name__ == "__main__":
    main()
