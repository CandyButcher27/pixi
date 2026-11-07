---
version: alpha
name: Blueprint-portfolio
description: An engineering-schematic portfolio treatment. A crosshair cursor with a live X/Y readout stands in for a drafting tool, corner registration marks frame the page like a print sheet, and projects are laid out as numbered spec panels (FIG. 1.A/B/C) with dimension-line dividers. One accent (cyan in dark mode, deep teal ink in light) carries every interactive signal; a second, orange, is reserved for annotation labels only.

colors:
  bg: "#0E1A2E"
  bg-elevated: "#12233B"
  ink: "#EAF3F5"
  ink-dim: "#8FA8B8"
  accent: "#5FD3E8"
  accent2: "#FF6A2B"
  grid-line: "rgba(95,211,232,0.12)"
  border: "rgba(95,211,232,0.28)"
  bg-light: "#F3EEDF"
  ink-light: "#1B2A3A"
  accent-light: "#1C6E8C"
  accent2-light: "#C1461A"

typography:
  display:
    fontFamily: "ui-monospace, SF Mono, JetBrains Mono, Consolas, monospace"
    weight: 500
    use: "Hero name, section heads — annotation/measurement voice"
  body:
    fontFamily: "-apple-system, Segoe UI, system-ui, sans-serif"
    weight: 400
    use: "Paragraph copy inside panels, role line"
  utility:
    fontFamily: "ui-monospace, SF Mono, Consolas, monospace"
    weight: 400
    use: "Coordinate readout, FIG labels, stat numbers"

spacing:
  grid-cell: 48px
  panel-pad: 32px
  section-gap: 120px

components:
  reg-mark:
    description: "Crosshair registration tick, fixed to each viewport corner — print/drafting-sheet framing device"
  crosshair-cursor:
    description: "Full-height/width guide lines following the pointer, plus a small coordinate readout chip (X:###, Y:###)"
  spec-panel:
    description: "Project card styled as a schematic sheet — FIG index + year in header, dimension-dashed footer with a REF code and view link"
  stat-block:
    description: "Underlined number + label pair, used in the hero for years/systems/throughput"
---

## Overview

Blueprint reframes "developer portfolio" as a technical drawing sheet rather than a marketing page. The whole surface behaves like something a drafting tool would produce: a faint coordinate grid sits behind everything, a crosshair tracks the cursor with a live coordinate readout, and corner registration marks pin the viewport like a printed plate. Projects are not "cards" — they are **FIG. 1.A / 1.B / 1.C** spec panels, each closed out with a dimension-dashed footer carrying a reference code.

This avoids the two clichés it sits closest to: neon hacker-terminal (green-on-black) and generic dark-mode SaaS. Blueprint commits instead to a genuinely different reference object — engineering schematics — and follows that reference in typography (monospace annotation voice), color (cyan ink on navy, or navy ink on aged cyanotype paper in light mode), and structure (grid, FIG labels, dimension lines).

## Colors

- **Accent** (`#5FD3E8` dark / `#1C6E8C` light): every link, stat number, active nav state, FIG label. One accent, used consistently.
- **Accent2** (`#FF6A2B` dark / `#C1461A` light): reserved *only* for the eyebrow annotation line and FIG year — never used for interactive elements. Keeps the "annotation vs. action" distinction legible.
- **Ground**: navy `#0E1A2E` in dark mode; the light theme is a deliberate cyanotype-paper flip (`#F3EEDF`), not a naive inversion — ink darkens to `#1B2A3A` and the grid/border opacities are retuned so the paper doesn't wash out.

## Typography

Monospace carries the whole page — headline, labels, and coordinate readouts — because the concept's honesty depends on it: a blueprint's lettering *is* technical, not a display font pretending to be technical. Body copy breaks to a humanist sans so paragraphs stay readable at length.

## Layout & Motion

- Background coordinate grid at 48px cells, low-opacity, present on every section.
- Crosshair follower (disabled on touch/`prefers-reduced-motion`) with a coordinate chip that reads real `clientX`/`clientY`.
- Hero elements rise in staggered on load (headline → role line → stat row) rather than all at once.
- Project panels reveal via `IntersectionObserver` on scroll, staggered ~80ms apart.
- Magnetic CTA button in the footer offsets toward the cursor within a small radius.

## Components

- **reg-mark** — four fixed crosshair ticks, one per corner, always present.
- **crosshair-cursor** + **coord-readout** — pointer-tracking guide lines and a small floating label.
- **spec-panel** — the project unit: FIG index + year header, title, description, tag chips, dimension-dashed footer with REF code + view link.
- **stat-block** — number over label, hairline rule above, used three times in the hero.

## Do's and Don'ts

### Do
- Keep the accent to one hue; let accent2 stay purely annotative.
- Reference real coordinates/labels (FIG 1.A, REF codes) — the numbering should look like it means something.
- Disable the crosshair follower under `(hover: none)` and `prefers-reduced-motion`.

### Don't
- Don't add a second interactive accent color — it breaks the "one pen, one ink" logic of a drafting sheet.
- Don't round the panel corners or add card shadows — the flat, ruled-line aesthetic is the point.
