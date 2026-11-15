"""Screenshot a built page and score how much of the recurring Claude house style it carries.

  uv run python scripts/pixi_check.py <page.html>           # simple tier: one static page
  uv run python scripts/pixi_check.py <project>/dist/index.html   # advanced tier: built React app

Writes <page dir>/pixi-shot.png (full page, 1440 wide) and prints the house-style traits found,
the running animation count, requestAnimationFrame callbacks per second and any console errors. Pages are served over HTTP so module scripts
load. For a dist/ build the house-style text comes from the project's own source (index.html and
src/), not the bundled component library CSS.
"""
import functools
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from blind import house_style  # noqa: E402
from designmcp import measure  # noqa: E402


FLASH_LIMIT = 3
OPACITY_TRACKS = """document.getAnimations().map(a => {
  const t = a.effect.getComputedTiming();
  const ops = a.effect.getKeyframes().map(k => k.opacity).filter(v => v !== undefined).map(Number);
  return {name: a.animationName || a.id || '', duration: t.duration, iterations: t.iterations, opacity: ops};
})"""
REDUCED_PROBE = """document.getAnimations().filter(a => a.playState === 'running' && a.effect.getComputedTiming().iterations === Infinity).length"""


def flash_rate(opacity: list[float], duration_ms: float) -> float:
    if len(opacity) < 2 or not duration_ms:
        return 0.0
    swings = sum(abs(b - a) >= 0.5 for a, b in zip(opacity, opacity[1:] + opacity[:1]))
    return swings / 2 / (duration_ms / 1000)


def flashes(tracks: list[dict]) -> list[str]:
    out = []
    for t in tracks:
        if t["iterations"] in (None, 0, 1) or not isinstance(t["duration"], (int, float)):
            continue
        rate = flash_rate(t["opacity"], t["duration"])
        if rate > FLASH_LIMIT:
            out.append(f"{t['name'] or 'animation'} {rate:.1f}/s")
    return out


def reduced_motion(url: str) -> tuple[int, int]:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
        page.add_init_script("window.__raf=0;const r=window.requestAnimationFrame.bind(window);window.requestAnimationFrame=f=>{window.__raf++;return r(f)};")
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(2500)
        loops = page.evaluate(REDUCED_PROBE)
        start = page.evaluate("window.__raf")
        page.wait_for_timeout(1000)
        raf = page.evaluate("window.__raf") - start
        browser.close()
    return loops, raf


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args) -> None:
        pass


def source_text(page_file: Path) -> str:
    if page_file.parent.name != "dist":
        return page_file.read_text(encoding="utf-8", errors="ignore")
    project = page_file.parent.parent
    files = [project / "index.html", *(p for p in (project / "src").rglob("*") if p.suffix in {".css", ".jsx", ".tsx", ".js", ".ts"})]
    return "\n".join(f.read_text(encoding="utf-8", errors="ignore") for f in files if f.exists())


def main() -> None:
    page_file = Path(sys.argv[1]).resolve()
    shot = page_file.with_name("pixi-shot.png")
    server = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(page_file.parent)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    errors: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.add_init_script("window.__raf=0;const r=window.requestAnimationFrame.bind(window);window.requestAnimationFrame=f=>{window.__raf++;return r(f)};")
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: m.type == "error" and errors.append(m.text))
        page.goto(f"http://127.0.0.1:{server.server_port}/{page_file.name}", wait_until="networkidle")
        page.wait_for_timeout(1500)
        height = page.evaluate("document.documentElement.scrollHeight")
        for y in range(0, height, 450):
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(120)
        page.wait_for_timeout(1800)
        animations = page.evaluate("document.getAnimations().length")
        flashing = flashes(page.evaluate(OPACITY_TRACKS))
        raf_start = page.evaluate("window.__raf")
        page.wait_for_timeout(1000)
        raf_per_second = page.evaluate("window.__raf") - raf_start
        body_bg = page.evaluate("getComputedStyle(document.body).backgroundColor")
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(500)
        page.screenshot(path=str(shot), full_page=True)
        browser.close()
    reduced_loops, reduced_raf = reduced_motion(f"http://127.0.0.1:{server.server_port}/{page_file.name}")
    server.shutdown()
    bg = body_bg if page_file.parent.name == "dist" else (measure.measure(page_file).get("backgrounds") or [""])[0]
    hits = house_style(source_text(page_file), bg)
    print(f"screenshot: {shot}")
    print(f"house style: {len(hits)}/7 {', '.join(hits) or '-'}  (lower is less Claude-looking; 3 or less is good)")
    print(f"motion: {animations} running CSS/SVG animations after scroll (0 means a static page)")
    print(f"motion: {raf_per_second} requestAnimationFrame callbacks per second after scroll (0 means no scripted motion)")
    print(f"flashing: {', '.join(flashing) or 'none'}  (opacity swings above {FLASH_LIMIT}/s are a seizure risk; fix any)")
    print(f"reduced motion: {reduced_loops} infinite CSS animations, {reduced_raf} requestAnimationFrame callbacks per second  (both should be 0)")
    print(f"console errors: {len(errors)}" + (f"  first: {errors[0][:200]}" if errors else ""))


if __name__ == "__main__":
    main()
