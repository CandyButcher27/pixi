---
version: alpha
name: Physics-playground-portfolio
description: Projects rendered as physical blocks in a hand-built gravity simulation — drag them, throw them, flip gravity, shake the table. A pool-table green ground and mustard/coral/teal blocks stand in for a workshop tabletop rather than a generic gradient hero.

colors:
  bg: "#0F3D2E"
  bg-soft: "#134634"
  ink: "#F5EFE0"
  ink-dim: "#A9C2B6"
  accent-mustard: "#E8B94A"
  accent-coral: "#E85C4A"
  accent-teal: "#3FA796"
  bg-light: "#EFE7D4"
  ink-light: "#1E2A22"

typography:
  display:
    fontFamily: "-apple-system, Segoe UI, system-ui, sans-serif"
    weight: 800
    use: "Hero headline, block titles — chunky, toy-like weight"
  body:
    fontFamily: "-apple-system, Segoe UI, system-ui, sans-serif"
    weight: 400
    use: "Lede paragraph, modal descriptions"
  utility:
    fontFamily: "ui-monospace, SF Mono, Consolas, monospace"
    use: "Arena hint text only"

spacing:
  arena-height: "min(560px, 62vh)"
  block-width: 200px

components:
  arena:
    description: "Bordered, dotted-grid play area containing all draggable project blocks — floor and walls the sim collides against"
  block:
    description: "A single project rendered as a colored, rounded rectangle with physical mass — falls, bounces, collides with siblings, and can be dragged/thrown"
  action-bar:
    description: "Three buttons above the arena: drop the work (respawn), flip gravity (invert), shake it (random impulse) — direct manipulation of the simulation, not decoration"
  modal:
    description: "Case-study detail opened by a genuine click (not a drag) on a block"
---

## Overview

Physics turns "here are my projects" into a literal toy: four colored blocks sit in a bordered arena and obey a small hand-written physics loop — gravity, wall/floor bounce, pairwise collision resolution, and drag-to-throw with real velocity capture from pointer movement. Nothing here comes from a physics library; the simulation (~40 lines of vector math) is intentionally simple so it stays predictable to play with.

The palette avoids both portfolio clichés it's adjacent to: it isn't a rainbow "fun/playful" palette, and it isn't the generic purple-blue gradient hero. Instead it commits to one physical reference — a pool table / workshop tabletop — mustard, coral, and teal blocks on felt green, which reads as considered rather than decorative.

## Colors

- **Ground** (`#0F3D2E` dark / `#EFE7D4` light): a felt-green "table," not a generic dark UI background.
- **Block colors** (mustard `#E8B94A`, coral `#E85C4A`, teal `#3FA796`, plus ink-colored cream for the resume block): four colors, each block keeps its color across both themes — the blocks are physical objects, not themed UI.
- Only mustard doubles as the interactive accent (buttons, stat numbers) — the other two stay block-only so they don't compete for "click me" attention.

## Typography

Heavy weight (800) sans at display sizes gives the "toy block" chunkiness the concept needs; body text drops to regular weight so it doesn't fight the blocks for attention. No serif, no mono display — mono is reserved for the one small arena hint label.

## Layout & Motion

- `requestAnimationFrame` loop: gravity accel, friction, wall/floor collision with damping, then O(n²) pairwise AABB overlap resolution between blocks — fine at 4-5 bodies.
- Drag capture uses the last 5 pointer samples to compute a real release velocity (a "throw"), not just a snap-to-cursor.
- Click vs. drag is disambiguated by movement distance + elapsed time, so tapping a settled block opens its case study without accidentally triggering on a throw.
- "Flip gravity" and "shake it" are direct, visible manipulations of the same simulation state — no separate animation system bolted on for effect.

## Components

- **arena** — bordered play area with a dotted grid, floor/walls the blocks bounce against.
- **block** — physical project unit: tag, title, one-line description, drag/throw/click-to-open behavior.
- **action-bar** — drop / flip gravity / shake buttons.
- **modal** — opened only on genuine click, full case study + stack tags + live link.

## Do's and Don'ts

### Do
- Keep the simulation legible — damping high enough that blocks settle, not perpetual chaos.
- Let each block keep its assigned color in both themes; only the ground and text tokens should flip.
- Disambiguate click vs. drag by both distance *and* time, not distance alone.

### Don't
- Don't reach for a physics library (Matter.js, etc.) — CSP blocks CDN scripts in this context, and the hand-rolled version is simpler to reason about at this scale.
- Don't let more than ~5 bodies exist at once — the O(n²) collision pass isn't built to scale further.
- Don't use a gradient hero — the arena itself is the hero.
