"""MCP server over the design catalogue. stdio transport.

  list_designs          the whole corpus, one line per entry
  search_designs        near / contrast / outlier reference triple for a brief
  get_design            one entry's measured grammar and where its source lives
  get_design_contract   the inherited constraints to build against
  verify_build          measure a built page against those constraints
"""
from __future__ import annotations

import json
from pathlib import Path

from mcp.server.mcpserver import MCPServer

from . import catalogue, contract as contract_mod, verify as verify_mod

ROOT = Path(__file__).resolve().parent.parent
SLOP_LAW = Path(__file__).resolve().parent / "slop_law.md"

mcp = MCPServer("design-catalogue")


@mcp.tool()
def list_designs() -> str:
    """Every design in the catalogue, one line each: id, kind, and its composition grammar."""
    lines = catalogue.index_lines()
    return f"{len(lines)} designs\n\n" + "\n".join(lines)


@mcp.tool()
def search_designs(brief: str) -> str:
    """Pick three references for a build brief.

    Returns a near reference (fits the brief), a contrast reference (furthest usable
    grammar), and an outlier (rarest grammar in the corpus). Nearest-three would push
    the build toward the middle of the design space; this deliberately does not.
    """
    refs = catalogue.select(brief)
    out = []
    for role, r in refs.items():
        g = r["grammar"]
        out.append(
            f"## {role}: {r['id']}  ({r['collection']}, relevance {r['relevance']}, "
            f"novelty {r['novelty']}, distance from near {r['distance_from_near']})\n"
            f"{g['hero_alignment']} hero (weight {g['hero_weight_split']}), {g['section_rhythm']} rhythm, "
            f"{g['full_bleed_sections']} full-bleed sections, {g['card_reliance']} card use "
            f"(largest row {g['largest_card_row']}), {g['geometry']} geometry (max radius {g['max_radius']}px), "
            f"display dominance {g['display_dominance']}x, {g['imagery']} imagery, {g['density']} density\n"
            f"source: {r['path'] if r['collection'] == 'live' else r['path'] + '/index.html'}"
        )
    return "\n\n".join(out) + "\n\nNext: call get_design_contract with this same brief."


@mcp.tool()
def get_design(design_id: str, include_source: bool = False) -> str:
    """One entry's measured composition grammar. Source markup only if you ask for it —
    reading the markup produces a clone, reading the grammar produces a new design."""
    entries = catalogue.load()
    if design_id not in entries:
        return f"unknown design '{design_id}'. Call list_designs for the catalogue."
    e = entries[design_id]
    body = [f"# {design_id} ({e['collection']})", "", "## composition grammar",
            json.dumps(e["grammar"], indent=2), "", "## retrieval text", e["text"][:1200]]
    if e["collection"] == "live":
        body += ["", f"live site, no local source: {e['path']}"]
    elif include_source:
        html = ROOT / e["path"] / "index.html"
        body += ["", "## source", html.read_text(encoding="utf-8", errors="ignore")[:20000]]
    else:
        body += ["", f"source available at {e['path']}/index.html (pass include_source=true)"]
    return "\n".join(body)


@mcp.tool()
def get_design_contract(brief: str, freeze_dir: str = "") -> str:
    """The inherited half of the design contract for this brief.

    Composition mandates come from the contrast and outlier references; prohibitions
    come from the anti-slop law. Write the rest of the contract yourself into
    DESIGN_CONTRACT.md — you may add constraints, never weaken these — then build
    against it and call verify_build.

    Pass freeze_dir (the directory you are about to build in) to freeze this contract to
    disk. Selection is then fixed before the page exists: verify_build reads the frozen
    file, so a disappointing page can never be rescued by retrieving a more convenient
    reference afterwards.
    """
    if freeze_dir:
        c, frozen = contract_mod.freeze(brief, ROOT / freeze_dir)
        note = ("\n\n> Contract frozen at " + c["frozen_at"] +
                (" (existing freeze reused — selection is fixed)" if not frozen else "") +
                f". verify_build will check against {freeze_dir}/contract.json.\n")
    else:
        c = contract_mod.build(catalogue.select(brief))
        note = "\n\n> Not frozen. Pass freeze_dir to fix this selection before building.\n"
    return contract_mod.as_markdown(c, brief) + note + "<!-- machine-readable -->\n```json\n" + \
        json.dumps(c["inherited"], indent=2) + "\n```\n"


@mcp.tool()
def verify_build(page_path: str, brief: str) -> str:
    """Render a built page and check it against the contract for this brief.

    Checks positive composition mandates first. Avoiding the prohibitions alone is not
    a pass — a page can dodge every AI tell and still be generic.
    """
    target = Path(page_path)
    if not target.is_absolute():
        target = ROOT / page_path
    if not target.exists():
        return f"no such page: {target}"
    c, source = contract_mod.load_frozen(target.parent)
    if c is None:
        c = contract_mod.build(catalogue.select(brief))
        source = "re-selected at verify time (NOT frozen — the references may differ from the ones you built against)"
    return f"contract: {source}\n" + verify_mod.report(verify_mod.verify(target, c))


@mcp.tool()
def get_slop_law() -> str:
    """The anti-slop design law: the tells of AI-generated design and what to do instead."""
    return SLOP_LAW.read_text(encoding="utf-8")


def main():
    mcp.run()


if __name__ == "__main__":
    main()
