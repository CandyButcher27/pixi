"""Render every catalogue entry and write designmcp/catalog.json.

Composition grammar comes from measuring the render, not from a model, so this runs
offline with no API key. Optional metadata.json (VLM whole-page tags) is folded in
for retrieval text when present.

Usage:
  .venv/Scripts/python.exe scripts/annotate_designs.py            # whole catalogue
  .venv/Scripts/python.exe scripts/annotate_designs.py stripe nike
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from designmcp import measure  # noqa: E402
from designmcp.catalogue import CATALOG, COLLECTIONS  # noqa: E402

TAG_RE = re.compile(r"<(title|h1|h2)[^>]*>(.*?)</\1>", re.I | re.S)


def retrieval_text(site_dir: Path) -> str:
    meta = site_dir / "metadata.json"
    if meta.exists():
        data = json.loads(meta.read_text(encoding="utf-8"))
        if data.get("embedding_text"):
            return data["embedding_text"]
    for spec in list(site_dir.glob("DESIGN-*.md")) + [site_dir / "design.md"]:
        if spec.exists():
            return spec.read_text(encoding="utf-8", errors="ignore")[:2000]
    html = (site_dir / "index.html").read_text(encoding="utf-8", errors="ignore")
    return " ".join(re.sub(r"<[^>]+>", " ", m.group(2)) for m in TAG_RE.finditer(html))[:2000]


def entries_to_render(only: set[str]) -> list[Path]:
    pages = []
    for collection in COLLECTIONS:
        for site_dir in sorted((ROOT / collection).iterdir()):
            if not site_dir.is_dir() or not (site_dir / "index.html").exists():
                continue
            if only and site_dir.name not in only:
                continue
            pages.append(site_dir / "index.html")
    return pages


def main():
    only = set(sys.argv[1:])
    pages = entries_to_render(only)
    if not pages:
        sys.exit("no entries matched")
    print(f"measuring {len(pages)} entries")

    measured = measure.measure_many(pages)
    existing = json.loads(CATALOG.read_text(encoding="utf-8"))["entries"] if CATALOG.exists() else {}

    failed = []
    for page in pages:
        site_dir = page.parent
        raw = measured[site_dir.name]
        g = measure.grammar(raw)
        if "error" in g:
            failed.append(f"{site_dir.name}: {g['error']}")
            continue
        existing[site_dir.name] = {
            "collection": site_dir.parent.name,
            "path": str(site_dir.relative_to(ROOT)).replace("\\", "/"),
            "grammar": g,
            "text": f"{site_dir.name} {retrieval_text(site_dir)}",
        }
        print(f"  {site_dir.name}: {g['hero_alignment']} hero, {g['section_rhythm']} rhythm, "
              f"{g['card_reliance']} cards, {g['geometry']}, {g['density']} density")

    CATALOG.write_text(json.dumps({"entries": existing}, indent=2), encoding="utf-8")
    print(f"\n{len(existing)} entries -> {CATALOG.relative_to(ROOT)}")
    if failed:
        print(f"{len(failed)} failed:")
        for f in failed:
            print(f"  {f}")


if __name__ == "__main__":
    main()
