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
- **Simple** (default): one self-contained `index.html` (inline CSS/JS, no external
  fonts or scripts, no build step) in `pixi/` at the project root. Opens by double-click.
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

## 3. Write the spec

Before any code, write `spec.md` next to the page: a 600-1000 word build brief in this order.
Building from your own full spec, instead of from rules, is how the Fable 5.2 gallery
(miaai-lab.github.io/Claude-Fable-5.2-HTML-Files, 76 pages with their prompts) avoids the default look.

- **Concept**: one line naming the metaphor the whole page lives inside, taken from the
  project ("the brand is the drawing", "the tins are the heroes, and one of them opens").
- **Material**: the physical medium every surface is made of (a cyanotype blueprint, a tin
  wrapper, a ledger, a lab notebook) and its texture: grain, creases, halftone, off-register ink.
- **Mood** in a few words, then a **palette** of about 5 named hex colours, with which one is
  reserved for the single call to action or for changing values.
- **Typography**: system font stacks chosen for character (Georgia italic, Impact,
  "Arial Narrow", Palatino, Menlo, Courier), named per role. No web fonts.
- **Structure**: numbered sections, each with its exact copy quoted: headline, subline, labels,
  real numbers from the project.
- **Signature moment**: one interaction specified down to the mechanics: what the user does
  (scroll, drag, click, type), what moves, how it eases, what the project's real data does in it.
- **Motion**: the entrance choreography (what draws itself first and last, over how long), what
  moves on its own with no input (an idle loop or a cycle), and what reacts to the pointer.
- **Reduced motion**: the still or slowed version, designed, not just switched off.

## 4. Build

Build from `spec.md`. Where the code and the spec disagree, change the spec first.

- **Borrow the reference's visual language**: typography character, colour, contrast, texture,
  mood. Do not copy its layout, content, logo or brand.
- **Original illustration is a primary surface.** Draw substantial art yourself in SVG or
  canvas (or use the project's real images). It carries whole sections, not a corner.
- **None of the default AI landing page**: no gradient backdrops, glass panels, pill CTAs,
  centred hero over three equal cards, or Inter/system-ui display type. No external scripts
  or fonts: everything inline.
- **Specific copy** from the project: real names, numbers, features. No three-word value props.
- **The page is alive, not just revealed.** Motion comes from the illustration and the
  mechanism, driven by `requestAnimationFrame`, springs and noise rather than fade-ins:
  - the signature moment works, on the project's real data where there is any;
  - an entrance draws the page in sequence (`stroke-dashoffset`, clip-path wipes, counters);
  - something keeps moving with no input, and the page acts on its own when the pointer is idle;
  - the pointer is a tool in the page's world (a crosshair with coordinates, a stamp, a probe),
    and interactions also work by keyboard and touch.
  Scroll reveals are optional and never the only motion. Cap `devicePixelRatio` at 2 for
  canvas, pause loops on `visibilitychange`, and implement the spec's reduced-motion version
  under `prefers-reduced-motion: reduce`.

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

## 5. Check

```
uv run --project PIXI python PIXI/scripts/pixi_check.py <path/to/index.html>
uv run --project PIXI python PIXI/scripts/pixi_check.py <project>/pixi-react/dist/index.html
```

Open the `pixi-shot.png` it writes and fix overlaps, cropped text and empty halves. It also
prints a house-style score; above 3 of 7, push further toward the reference. It counts running
CSS/SVG animations and `requestAnimationFrame` callbacks per second after scrolling; both 0
means the page is static, so go back to the motion rule. Any console error is a bug to fix. Report the page
path, the spec path, the reference URL used, and the score; for the advanced tier also how to run it
(`npm run dev`, or `npm run preview` after a build).

## 6. Record it in the progression catalogue

`C:\Users\sriva\Desktop\Hackathons\catalogue\catalogue.json` tracks every project through every
pixi stage. Add the new build as that project's entry for its stage (page, spec, shots, ref,
score, one-line note). When the method itself changed, append a new stage with its date and what
changed, and build the page into a new folder (`pixi-v3/`, ...) so earlier stages stay viewable.
Then rebuild and fix anything it lists as missing:

```
uv run --project PIXI python PIXI/scripts/build_catalogue.py C:/Users/sriva/Desktop/Hackathons/catalogue/catalogue.json
```

## Optional: the catalogue protocol

For reference-driven builds inside the pixi repo only: `search_designs` -> `get_design_contract`
-> build -> `verify_build` on the `design-catalogue` MCP server (or `scripts/design_cli.py`).
Not the default: blind ratings found it no better than the prompt rules (DEC-15).
