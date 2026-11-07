---
version: alpha
name: Woven-loom-portfolio
description: A textile-loom portfolio. SVG threads draw themselves in on load and on scroll (stroke-dashoffset animation), projects sit as woven fabric "patches" with a thread-pull hover effect, and the palette (indigo, rust, undyed linen) is drawn from dyed cloth rather than digital UI conventions.

colors:
  bg: "#22201B"
  panel: "#2A2721"
  ink: "#F1E9D8"
  dim: "#A79E8A"
  accent: "#5A79B8"
  accent2: "#C97A45"
  thread: "rgba(241,233,216,0.16)"
  bg-light: "#EFE7D3"
  ink-light: "#2A2A22"
  accent-light: "#2E4570"
  accent2-light: "#A2481F"

typography:
  display:
    fontFamily: "Segoe UI, -apple-system, system-ui, sans-serif"
    weight: 800
    use: "Headlines, patch titles — warm rounded-feeling sans, distinct from Starchart's serif and Blueprint/Terminal's monospace"
  body:
    fontFamily: "Segoe UI, -apple-system, system-ui, sans-serif"
    weight: 400
    use: "Lede, about paragraph"

spacing:
  fabric-gap: 4px
  patch-pad: 22px
  weave-divider-height: 90px

components:
  weave-svg:
    description: "Generated SVG grid of warp/weft paths with stroke-dasharray set to each path's own length; animates to dashoffset 0 to look hand-drawn/woven-in"
  patch:
    description: "A project rendered as a fabric square in a tight grid; hover reveals an accent2 thread along the left edge and lifts the patch slightly, like pulling a loose thread taut"
  weave-divider:
    description: "A thin horizontal weave strip between sections, triggered by IntersectionObserver so it draws in only once scrolled into view"
---

## Overview

Woven treats the portfolio's structure as literal cloth: the hero background is a generated grid of SVG "warp and weft" threads that draw themselves in with a `stroke-dasharray`/`stroke-dashoffset` animation on load, and projects sit as square fabric "patches" in a tight, gapless grid — thread-colored dividers between them rather than card borders. Section breaks reuse the same weave-drawing technique as thin horizontal dividers, triggered once each scrolls into view.

The palette is pulled from dyed textile, not from any digital reference: indigo (warp thread) and rust (weft thread) against undyed linen or dark walnut — deliberately avoiding both the neon-tech palette family and the cream/terracotta "AI generated" default, since neither belongs to the textile world this concept is drawing from.

## Colors

- **Accent** (`#5A79B8` indigo / `#2E4570` deep indigo light): links, patch tag text — the "warp thread" color.
- **Accent2** (`#C97A45` rust / `#A2481F` burnt rust light): the hover-reveal thread on each patch and the eyebrow label — the "weft thread" color, used only as a highlight, never as the primary interactive hue.
- Ground is walnut-dark or undyed-linen-light — genuinely warm neutrals, not a grey scale with a hue tint.

## Typography

A warm, rounded-reading system sans at heavy weight for headlines — chosen specifically to differ from every other concept's display face in this set (Blueprint/Terminal are monospace, Starchart is an italic serif). No monospace anywhere; a woven-cloth concept has no reason to reference a technical readout.

## Layout & Motion

- `buildWeaveSVG()` generates warp (horizontal) and weft (vertical) paths procedurally for a given row/column count, each with a computed path length used to drive its own `stroke-dasharray`.
- On load, the hero weave draws in with a staggered per-path delay (~30ms apart). Section-divider weaves use the same function but wait for `IntersectionObserver` before drawing, and only draw once (`unobserve` after triggering).
- Patch hover: a left-edge accent2 bar scales in from `scaleY(0)` to `scaleY(1)`, paired with a small `translateY(-4px)` lift — reads as "pulling a thread taut," not a generic card-hover shadow.
- `prefers-reduced-motion` skips all dash-offset transitions; the weave renders instantly at its final state.

## Components

- **weave-svg** — the procedural thread-drawing system, reused for both the hero background and the thin section dividers.
- **patch** — the project unit, laid out edge-to-edge in a `--thread`-colored grid gap so the gap itself reads as stitching.
- **weave-divider** — scroll-triggered thin weave strip marking section boundaries.

## Do's and Don'ts

### Do
- Reuse one procedural weave function for both the large hero background and the thin dividers — consistency of technique is what sells the "cloth" metaphor.
- Keep accent2 confined to hover/highlight moments — it's a weft thread, not a primary action color.
- Size the patch grid gap to read as stitching (`background` color showing through a small `gap`), not as a visible border.

### Don't
- Don't forget to apply the shared path-styling rule to *every* generated `<svg>` in the page — an SVG missing the `stroke`/`fill:none` rule renders its paths with the browser default (black fill), which is exactly the rendering bug this build hit and fixed.
- Don't use a cream/terracotta palette — it's the generic "AI-generated design" default this concept specifically avoids.
- Don't add a monospace utility face — nothing in a woven-cloth concept should read as a technical readout.
