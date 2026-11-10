---
name: pixi
description: Build a distinctive frontend (landing page or marketing site) for the current project, borrowing visual language from a real site screenshot instead of the default Claude look. Use when the user runs /pixi, or asks for a landing page, marketing site or portfolio page.
---

# pixi

Pixi home (scripts and reference harvest): `C:\Users\sriva\Desktop\Projects\Agents\frontend-agent`,
called `PIXI` below. Run its scripts with `uv run --project PIXI python PIXI/scripts/<name>.py`.

This setup won blind human ratings: original illustration plus a screenshot reference was
preferred 4–1 over illustration alone, and cut the recurring Claude house style (cream paper,
Fraunces, mono labels, numbered sections, italic headline word) from 5.0 to 3.0 of 7. Evidence:
`PIXI/builds/blind/RESULTS.md`.

## 1. Get the context

Read the project before writing anything: README, package/pyproject metadata, existing pages,
copy, logos, brand colours. Write a one-line brief ("landing page for <what> for <whom>").
Ask the user one question only if the purpose is unclear.

**Pick the tier.** Unless the user already said, ask once:
- **Simple** (default): one self-contained `index.html` (inline CSS/JS, Google Fonts allowed,
  no build step) in `pixi/` at the project root. Opens by double-click.
- **Advanced**: a React 19 + Astryx app (Vite) in `pixi-react/` at the project root, built
  around a working demo of the project on its real data. Needs Node; served, not double-clicked.

## 2. Pick a reference

```
uv run --project PIXI python PIXI/scripts/pick_reference.py "<brief>" -n 5
```

It returns screenshot candidates outside the house style, from the local gallery harvest or,
when that runs short, fetched fresh through scrappy (`Agents/scraping-agent`) after a
robots.txt check.

**Visual check:** open each screenshot with the file-reading tool, in order. Reject it if it is
broken or unusable as design: an age gate, a cookie or consent wall covering most of it, error
or PHP warning text, a blank or loading screen, or a plain corporate page with nothing to
learn from. Use the first good one. If none pass, build without a reference and say so.

## 3. Build

- **Borrow the reference's visual language**: typography character, colour, contrast, texture,
  mood. Do not copy its layout, content, logo or brand.
- **Original illustration is a primary surface.** Draw substantial art yourself in SVG or
  canvas (or use the project's real images). It carries whole sections, not a corner.
- **None of the default AI landing page**: no gradient backdrops, glass panels, pill CTAs,
  centred hero over three equal cards, or Inter/system-ui display type.
- **Specific copy** from the project: real names, numbers, features. No three-word value props.
- **The page moves.** Animate the illustration itself, the way showcase sites loop project
  video: threads marching, parts swinging, counters ticking, a drawing that turns. Reveal
  sections with transform and opacity over 1.5s on `cubic-bezier(.19,1,.22,1)` via
  IntersectionObserver. Where the project has a mechanism, make one small working demo of it.
  Wrap everything in `prefers-reduced-motion: reduce`.

### Advanced tier: React + Astryx

Same visual rules, plus:
- Scaffold `pixi-react/` with Vite, `react`/`react-dom` 19, `@astryxdesign/core`,
  `@astryxdesign/theme-neutral`, `@stylexjs/stylex`, dev `@astryxdesign/cli` and
  `@vitejs/plugin-react`; `base: './'` in `vite.config.js`. Import `reset.css`, `astryx.css`,
  the theme's `theme.css` in that order, wrap the app in `<Theme theme={neutralTheme}>`.
- Look components up with `npx @astryxdesign/cli component <Name>` (`--list` for all 174) and
  tokens with `npx @astryxdesign/cli docs tokens`. Never guess props.
- Re-skin by overriding Astryx tokens (`--color-background-body`, `--color-text-primary`,
  `--color-accent`, `--color-error`, `--font-family-body`, ...) on the app's root element, not
  `:root`: the Theme wrapper sets them closer than `:root`.
- Feed the demo real project data: run the project's own code (in Python where it is Python)
  and write the output to `src/*.json`. Show disagreements in that data instead of hiding them.
- `npx vite build`, then check `pixi-react/dist/index.html` below.

## 4. Check

```
uv run --project PIXI python PIXI/scripts/pixi_check.py <path/to/index.html>
uv run --project PIXI python PIXI/scripts/pixi_check.py <project>/pixi-react/dist/index.html
```

Open the `pixi-shot.png` it writes and fix overlaps, cropped text and empty halves. It also
prints a house-style score; above 3 of 7, push further toward the reference. It counts running
CSS/SVG animations after scrolling; 0 means the page is static, so go back to the motion rule
(requestAnimationFrame motion is not counted). Any console error is a bug to fix. Report the page
path, the reference URL used, and the score; for the advanced tier also how to run it
(`npm run dev`, or `npm run preview` after a build).

## Optional: the catalogue protocol

For reference-driven builds inside the pixi repo only: `search_designs` -> `get_design_contract`
-> build -> `verify_build` on the `design-catalogue` MCP server (or `scripts/design_cli.py`).
Not the default: blind ratings found it no better than the prompt rules (DEC-15).
