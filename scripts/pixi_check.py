"""Screenshot a built page and score how much of the recurring Claude house style it carries.

  uv run python scripts/pixi_check.py <page.html>

Writes <page dir>/pixi-shot.png (full page, 1440 wide) and prints the house-style traits found.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from blind import house_style  # noqa: E402
from designmcp import measure  # noqa: E402


def main() -> None:
    page_file = Path(sys.argv[1]).resolve()
    shot = page_file.with_name("pixi-shot.png")
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(page_file.as_uri(), wait_until="load")
        page.wait_for_timeout(1500)
        page.screenshot(path=str(shot), full_page=True)
        browser.close()
    bg = (measure.measure(page_file).get("backgrounds") or [""])[0]
    hits = house_style(page_file.read_text(encoding="utf-8", errors="ignore"), bg)
    print(f"screenshot: {shot}")
    print(f"house style: {len(hits)}/7 {', '.join(hits) or '-'}  (lower is less Claude-looking; 3 or less is good)")


if __name__ == "__main__":
    main()
