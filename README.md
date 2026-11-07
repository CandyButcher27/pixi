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

## Using it

The `design-build` skill drives the protocol. In short:

1. `search_designs(brief)` — near / contrast / outlier references. Deliberately not the
   nearest three; three adjacent references push the build back toward the middle.
2. `get_design_contract(brief)` — inherited composition mandates plus prohibitions.
3. Write `DESIGN_CONTRACT.md`, adding the brief-specific decisions. Inherited
   constraints may be added to, never weakened.
4. Build the page.
5. `verify_build(page, brief)` — renders it and checks the mandates. A page that only
   avoids the prohibitions fails.

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
