---
name: design-build
description: Build a frontend page against the design catalogue instead of from defaults. Use whenever the user asks for a landing page, marketing site, portfolio, dashboard shell, or any new UI in this repo — before writing any markup.
---

# design-build

Left alone, a model builds the same page every time: centred hero, gradient, three
equal cards, pill CTA, Inter, testimonial strip, footer. That is mode collapse, not
missing knowledge. This protocol replaces the default mode with a constrained one.

The `design-catalogue` MCP server is the source of constraints. Do not skip it and
do not build "in the spirit of" its output.

## Protocol

1. **`search_designs(brief)`** — returns three references: near, contrast, outlier.
   Read all three grammars. The contrast and outlier are not decoration; they are
   where the differentiation comes from.
2. **`get_design_contract(brief, freeze_dir="<the directory you will build in>")`** —
   returns the design intent, the inherited composition mandates, and the prohibitions,
   and freezes that selection to disk. Always pass `freeze_dir`. Selection is fixed
   before the page exists, so a disappointing page can never be rescued by retrieving a
   more convenient reference afterwards.
3. **Write `DESIGN_CONTRACT.md`** next to the page you are about to build. Copy every
   inherited constraint verbatim, then add the brief-specific decisions that are
   yours: typefaces (never a generic default), palette, section order, copy, and how
   each mandate is realised structurally. **You may add constraints. You may never
   weaken, reinterpret, or drop an inherited one.**
4. **Build the page** against that contract. The mandates prevent known failure modes;
   the design intent is what they are for. Satisfying the numbers while violating the
   intent is a failed build — an alternating anchor whose other side is empty margin
   passes `centroid_flips` and fails the intent behind it.
5. **`verify_build(page_path, brief)`** — fix every violation and re-verify. Two
   iterations maximum; if it still fails, say which mandate you could not satisfy and
   why, rather than quietly relaxing it.

## Rules

- Read the grammar, not the markup. `get_design(id, include_source=true)` exists for
  when you need to see how a specific effect was implemented — reading it by default
  produces a clone of the reference instead of a new design.
- A page that satisfies every prohibition and no mandate has failed. Passing means the
  positive composition obligations are measurably present in the render.
- Without an MCP connection, the same thing is available as
  `.venv/Scripts/python.exe scripts/design_cli.py contract "<brief>" <dir>` and
  `... design_cli.py verify <dir>/index.html`.
- `get_slop_law()` is the long form of the prohibitions. Read it when the contract's
  one-line reasons are not enough.
