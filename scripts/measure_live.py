import json
import sys
from multiprocessing import Pool
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from designmcp.measure import PROBE, VIEWPORT, grammar  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITES = ROOT / "research/harvest/galleries/sites_merged.jsonl"
OUT = ROOT / "research/harvest/galleries/measured.jsonl"
SHOTS = ROOT / "research/harvest/galleries/screens"
WORKERS = 4
SETTLE_MS = 2500


def measure_chunk(urls: list[str]) -> list[dict]:
    rows = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for url in urls:
            ctx = browser.new_context(viewport=VIEWPORT)
            page = ctx.new_page()
            try:
                resp = page.goto(url, wait_until="load", timeout=30000)
                page.wait_for_timeout(SETTLE_MS)
                metrics = page.evaluate(PROBE)
                slug = url.split("//", 1)[-1].strip("/").replace("/", "_")[:120]
                SHOTS.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(SHOTS / f"{slug}.png"))
                rows.append({"url": url, "final_url": page.url, "status": resp.status if resp else None,
                             "metrics": metrics, "grammar": grammar(metrics)})
            except Exception as exc:
                rows.append({"url": url, "error": f"{type(exc).__name__}: {str(exc)[:200]}"})
            finally:
                ctx.close()
        browser.close()
    return rows


def main(min_galleries: int, limit: int | None) -> None:
    kept = []
    if OUT.exists():
        kept = [r for r in map(json.loads, OUT.read_text(encoding="utf-8").splitlines()) if "grammar" in r]
        OUT.write_text("".join(json.dumps(r) + "\n" for r in kept), encoding="utf-8")
    done = {r["url"] for r in kept}
    sites = [json.loads(line) for line in SITES.read_text(encoding="utf-8").splitlines()]
    urls = [s["url"] for s in sites if len(s["galleries"]) >= min_galleries and s["url"] not in done][:limit]
    chunks = [urls[i::WORKERS] for i in range(WORKERS)]
    with Pool(WORKERS) as pool, OUT.open("a", encoding="utf-8") as fh:
        for rows in pool.imap_unordered(measure_chunk, [c for c in chunks if c]):
            for row in rows:
                fh.write(json.dumps(row) + "\n")
    print(f"measured {len(urls)} sites -> {OUT}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2, int(sys.argv[2]) if len(sys.argv) > 2 else None)
