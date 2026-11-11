# What pixi takes from outside repositories

Everything under `research/` is a local, git-ignored mirror. This file records what pixi actually
uses from each source, where that now lives, and whether the mirror can be deleted. Checked
2026-11-11 by searching `scripts/`, `designmcp/`, `tests/`, `.claude/skills/` and every hackathon
`pixi*/` build for references.

## Needed: do not delete

### Gallery harvest: `research/harvest/galleries/` (206 MB)
Award-gallery site lists plus 509 full-page screenshots.
- `screens/*.png`: the screenshot references `scripts/pick_reference.py` returns. Every pixi
  build's reference (madebysix.com, garonzi1925.com, easings.co, wemadethat.co.uk, heyclicky.com)
  came from here.
- `measured.jsonl`, `sites_merged.jsonl`: read by `designmcp/catalogue.py` (the `live`
  collection) and written by `scripts/measure_live.py`.
- Rebuilding it means rerunning `harvest.py`, `merge.py`, `fetch.py` and `measure_live.py`:
  hours of network fetching.

## Used once, distilled, safe to delete

### meta/astryx: `research/astryx/` (642 MB, commit a5ad1f2, https://github.com/meta/astryx)
This is the React component library behind the advanced tier ("React + Astryx").
- **Nothing reads the clone.** The React builds install Astryx from npm:
  `@astryxdesign/core`, `@astryxdesign/theme-neutral` and `@astryxdesign/cli`, all 0.7.12, plus
  `@stylexjs/stylex`. Each `pixi-react/` has its own `node_modules`.
- Component docs come from the CLI, not the clone: `npx @astryxdesign/cli component <Name>`
  (`--list` for all 174), `npx @astryxdesign/cli docs tokens`.
- Components the five React builds use:

  | project | components |
  |---|---|
  | ClearPath | Badge, Button, Collapsible, ProgressBar, SegmentedControl |
  | Foundry | Button, Slider, Switch |
  | Ariadne | Badge, Button, CheckboxInput, Collapsible |
  | CoFounders | Badge, Banner, Switch |
  | NAVIK | Badge, Button, DateInput, NumberInput, SegmentedControl, Selector |

  Every build also imports `reset.css`, `astryx.css`, the `Theme` wrapper and `theme-neutral`.
- Quirks learned from it: re-skin by overriding Astryx tokens on the app's root element, not
  `:root`, because the `Theme` wrapper sets them closer (this one is in the skill). Astryx styles
  `p`/`h2` with its dark text token and its reset zeroes margin and padding, so on a dark section
  override `--color-text-primary` on that block and give padding a more specific selector.
- The simple and spec-first pages use nothing from Astryx. They are single static HTML files
  with no external scripts or fonts.

### Fable 5.2 gallery: `research/fable52/` (21 MB, https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files)
76 pages with their ~800-word prompts. It is the source of the spec-first stage: the spec order
in the pixi skill (concept, material, palette, typography, structure, signature moment, motion,
reduced motion) is taken from how those prompts are written. Measured: a named signature moment
76/76, a designed reduced-motion variant 76/76, `requestAnimationFrame` 71/76, canvas 55/76, no
external scripts or web fonts. The skill mentions this folder only as an example; the URL above
serves the same files.

### Nutlope/inspo screenshots: `research/harvest/Nutlope__inspo/` (7.3 GB)
Only `scripts/rate.py` reads it: a local pairwise rating page over these screenshots. No rating
file from it exists any more, and no build uses it. Largest single saving.

### Cloned design repos: `research/repos/` (997 MB) and the same repos under `research/harvest/<owner>__<name>/`
26 repositories read for prior art (anti-slop skills, taste skills, design-md collections, shader
and noise libraries, design-token packages). No pixi script or page imports code from any of
them. Each one is summarised in `research/reports/<owner>__<name>.md` (324 KB in total). Keep
`research/reports/`, delete the clones.
- `VoltAgent/awesome-design-md`: the `websites/*/DESIGN-*.md` specs came from it and are already
  copied into `websites/`.
- `stegu/webgl-noise`, `FarazzShaikh/glNoise`, `paper-design/shaders`: read, not used; pixi pages
  write their own noise.

### Design-system tokens: `research/harvest/design-system-tokens/` (33 MB)
101 official design systems at pinned commits. Nothing reads it; summary in
`research/reports/design-system-tokens.md`.

## Not a repository but used

- **scrappy** (`../scraping-agent`): `pick_reference.py` calls `uv run scrappy search` when the
  local gallery runs short. Needs `EXA_API_KEY`.
- **Playwright Chromium**: screenshots for `pixi_check.py` and `pick_reference.py`.
