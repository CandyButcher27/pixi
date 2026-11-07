"""Log the retrieval and contract half of a protocol run, before anything is built.

The point is traceability: if a built page turns out generic, this log says whether the
triple was bad or the agent ignored a good one.

Usage:
  .venv/Scripts/python.exe scripts/protocol_run.py                 # log triples + contracts
  .venv/Scripts/python.exe scripts/protocol_run.py --verify        # also verify built pages
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from designmcp import catalogue, contract as contract_mod, verify as verify_mod  # noqa: E402

BUILDS = ROOT / "builds"
BRIEFS = {
    "analytics": "developer analytics platform for backend engineers",
    "roaster": "independent coffee roaster in Lisbon",
    "caselaw": "legal case management software for small firms",
    "festival": "experimental electronic music festival",
    "robotics": "hardware robotics startup building warehouse arms",
}


def log_selection(slug: str, brief: str) -> dict:
    c, _ = contract_mod.freeze(brief, BUILDS / slug)
    refs = catalogue.select(brief)
    out = [f"## {slug} — \"{brief}\"", ""]
    for role, r in refs.items():
        g = r["grammar"]
        out.append(f"{role.upper()}  {r['id']}  (relevance {r['relevance']}, novelty {r['novelty']}, "
                   f"distance from near {r['distance_from_near']})")
        out.append(f"  {g['hero_alignment']} hero {g['hero_weight_split']} | {g['section_rhythm']} rhythm | "
                   f"{g['full_bleed_sections']} full-bleed | {g['card_reliance']} cards "
                   f"(row {g['largest_card_row']}) | {g['geometry']} {g['max_radius']}px | "
                   f"display {g['display_dominance']}x | {g['imagery']} imagery | {g['density']} density")
    out += ["", "CONTRACT (inherited)", f"  direction: {c['identity']['direction']}", "  required:"]
    for r in c["inherited"]["required"]:
        out.append(f"    {r['rule']} {r['op']} {r['value']}   <- {r['source']}")
    out.append("  forbidden:")
    for r in c["inherited"]["forbidden"]:
        out.append(f"    {r['rule']} {r['op']} {r['value']}   <- {r['source']}")
    return {"slug": slug, "brief": brief, "refs": refs, "contract": c, "lines": out}


def main():
    do_verify = "--verify" in sys.argv
    BUILDS.mkdir(exist_ok=True)
    sections = ["# Protocol run log", ""]
    for slug, brief in BRIEFS.items():
        run = log_selection(slug, brief)
        sections += run["lines"]
        page = BUILDS / slug / "index.html"
        if do_verify and page.exists():
            sections += ["", "VERIFICATION", verify_mod.report(verify_mod.verify(page, run["contract"]))]
        elif do_verify:
            sections += ["", "VERIFICATION: not built yet"]
        sections.append("")
    (BUILDS / "run-log.md").write_text("\n".join(sections), encoding="utf-8")
    print("\n".join(sections))


if __name__ == "__main__":
    main()
