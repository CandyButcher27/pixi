# Frontend

A design-decision compiler for coding agents. An agent asked for "a landing page for a
SaaS product" builds the same page every time — centred hero, gradient, three equal
cards, pill CTA, Inter. That is mode collapse, not missing knowledge. This repo replaces
the default mode with a constrained one: real design references, measured, turned into
composition mandates the built page is then checked against.

## Contents

- **`designmcp/`** — the MCP server the agent connects to, plus the machinery behind it:
  `measure.py` (composition grammar from a render), `catalogue.py` (reference
  selection), `contract.py` (constraint synthesis), `verify.py` (checking a built page),
  `slop_law.md` (the anti-slop design law), `catalog.json` (the annotated corpus).
- **`websites/`** — 77 standalone single-page homages of real brands
  (`<site>/index.html` + stylesheet + script + design spec). The primary corpus.
- **`portfolio-concepts/`** — 7 original, non-brand-derived concepts.
- **`video_animated/`** — scroll/video-driven builds, each with the build spec that
  produced it.
- **`scripts/`** — `annotate_designs.py` (renders and measures the corpus),
  `screenshot_sites.py`, `generate_metadata.py` (optional VLM whole-page tags),
  `regenerate_stub_site.py`.
- **`docs/`** — regeneration tracking and notes.

## Setup

```
pip install uv
uv sync
uv run playwright install chromium
.venv/Scripts/python.exe scripts/annotate_designs.py
```

The MCP server is registered in `.mcp.json` and needs no API key: composition grammar is
measured from the render, not inferred by a model.

## Using it: `/pixi`

The `pixi` skill (`.claude/skills/pixi/`) builds a frontend for whatever project it runs in:

1. Reads the project and writes a one-line brief.
2. `scripts/pick_reference.py "<brief>"` returns screenshots of real sites outside the
   recurring Claude house style, from a local gallery harvest or fetched fresh via the
   scrappy scraping agent (search only, robots.txt obeyed). The agent looks at each and
   rejects broken ones (age gates, cookie walls, error pages).
3. Builds one self-contained page that borrows the reference's visual language, with
   original SVG/canvas illustration as a primary surface and none of the default AI look.
4. `scripts/pixi_check.py page.html` screenshots it and scores the house style.

Why this setup: four blind human rating rounds in `builds/blind/RESULTS.md`. The full
catalogue protocol below did not beat a plain prompt; one illustration line matched it; a
screenshot reference on top won 4–1 and cut the house-style score from 5.0 to 3.0 of 7.

Install globally (so `/pixi` works in any project): copy `.claude/skills/pixi` to
`~/.claude/skills/pixi`. The scripts use absolute paths to this checkout. The reference
harvest under `research/` stays local and is not in this repo.

## The catalogue protocol (optional)

1. `search_designs(brief)` — near / contrast / outlier references.
2. `get_design_contract(brief)` — inherited composition mandates plus prohibitions.
3. Write `DESIGN_CONTRACT.md`; inherited constraints may be added to, never weakened.
4. Build the page.
5. `verify_build(page, brief)` — renders it and checks the mandates.

## Pipeline (optional VLM layer)

```
.venv/Scripts/python.exe scripts/screenshot_sites.py            # all sites
.venv/Scripts/python.exe scripts/generate_metadata.py stripe    # needs OLLAMA_API_KEY
```

`generate_metadata.py` adds whole-page semantic tags used for retrieval text. Config:
`config.yaml` (`ollama.host`, `ollama.model`) + `.env` (`OLLAMA_API_KEY`).

## Tests

```
.venv/Scripts/python.exe -m pytest tests -q
```

`tests/test_verify.py` includes the verifier's falsification case: a deliberately
generic page that satisfies every prohibition must still fail verification.
