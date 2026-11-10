---
name: design-build
description: Build a frontend page in this repo. Use whenever the user asks for a landing page, marketing site, portfolio, dashboard shell, or any new UI here — before writing any markup.
---

# design-build

Default: build straight from the brief, with the rules below. In blind human ratings
(`builds/blind/RESULTS.md`, 2026-11-10) the plain request plus one illustration rule
scored level with the full catalogue/contract protocol (6–4, p = 0.75) at a fraction of
the cost, so the protocol is no longer required.

## Rules

1. **Original illustration is a primary surface.** Draw substantial art yourself in SVG
   or canvas (or use real photography when the user provides it). Not decoration in a
   corner: it carries whole sections. Pages without it lost most head-to-heads.
2. **None of the default AI landing page.** No gradient backdrops, glass panels, pill
   CTAs, centred hero over three equal cards, or a generic display face (Inter,
   system-ui, Arial). `get_slop_law()` on the `design-catalogue` MCP server has the long
   form.
3. **Specific copy.** Real-sounding names, numbers and details for the brief, not
   three-word value propositions.
4. **Look at it.** Take a full-page screenshot before reporting done and fix what reads
   wrong: overlaps, cropped labels, empty halves.

## Optional: the catalogue protocol

Use only when the user asks for a reference-driven build. `search_designs(brief)` ->
`get_design_contract(brief, freeze_dir=<build dir>)` -> write `DESIGN_CONTRACT.md` ->
build -> `verify_build(page_path, brief)`, two repair rounds maximum, inherited rules
never weakened. Without MCP: `uv run python scripts/design_cli.py contract "<brief>" <dir>`
and `... design_cli.py verify <dir>/index.html`. Known faults: its imagery metric ignores
inline SVG, and its contracts forbid imagery for many briefs.
