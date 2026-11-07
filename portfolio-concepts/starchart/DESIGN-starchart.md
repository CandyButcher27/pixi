---
version: alpha
name: Starchart-atlas-portfolio
description: Projects rendered as labeled stars in a canvas starfield, joined by constellation lines, with parallax drift on mouse movement. Antique-atlas serif typography and a gold-on-void (flipping to bronze-on-parchment) palette root the concept in celestial cartography rather than generic sci-fi space.

colors:
  bg: "#05070D"
  panel: "#0C1020"
  ink: "#EAE6D8"
  dim: "#7C7A6E"
  accent: "#C9A24B"
  line: "rgba(201,162,75,0.35)"
  star: "#EAF0FF"
  bg-light: "#EFE7D0"
  ink-light: "#1B1B22"
  accent-light: "#8C6A1F"

typography:
  display:
    fontFamily: "Georgia, Iowan Old Style, Times New Roman, serif"
    style: italic
    use: "Headlines and section titles — old-atlas plate-caption voice"
  body:
    fontFamily: "-apple-system, Segoe UI, system-ui, sans-serif"
    use: "Lede paragraph, plate descriptions, modal body"
  utility:
    fontFamily: "ui-monospace, SF Mono, Consolas, monospace"
    use: "Not used — this concept deliberately has no monospace voice"

spacing:
  atlas-height: "82vh (min 520px)"
  plate-pad: 26px

components:
  canvas-sky:
    description: "Full-bleed canvas starfield: ~160 twinkling background stars plus labeled project-stars, connected by thin constellation lines, both layers parallax-shifted opposite the mouse position"
  project-star:
    description: "A project encoded as a canvas-drawn point with a Greek-letter label (α, β, γ, δ) and a fake RA/Dec coordinate — click opens the record"
  plate:
    description: "Below-the-fold project summary card styled like an atlas catalogue entry — figure number, italic title, short description"
---

## Overview

Starchart frames the portfolio as a star atlas: a canvas starfield sits behind the hero copy, background stars twinkle and drift with the cursor (parallax), and each project is a labeled "star" joined to the others by thin gold constellation lines. Clicking a star opens a modal styled like an atlas plate caption, complete with a fabricated celestial coordinate (`RA 04h12m · DEC +21°`) standing in for a project's timestamp.

The typographic choice — an italic serif reminiscent of 18th/19th-century star charts — is what keeps this from reading as generic "space/sci-fi" (which would default to a technical sans and neon). No monospace appears anywhere in this build; that's deliberate, since a coordinate readout in mono would tip the whole thing back toward "software UI" rather than "printed atlas."

## Colors

- **Accent** (`#C9A24B` gold / `#8C6A1F` bronze): star labels, constellation lines, headline emphasis — the single "ink" color throughout, evoking engraved gold leaf on old charts.
- **Star** (`#EAF0FF` dark / dark ink in light mode): the neutral dot color for background stars — distinct from the accent so labeled project-stars visually pop against the field.
- Light theme is a genuine material flip — void/parchment, not merely inverted lightness — so it reads as "the same atlas printed on paper" rather than a dark-mode toggle.

## Typography

Italic serif for every headline and label — the "plate caption" voice. Body copy is a plain sans for legibility at paragraph length; no monospace face is used anywhere, keeping the whole thing feeling like print rather than software.

## Layout & Motion

- Canvas redraws every frame: background stars twinkle via a sine-based alpha pulse; foreground project-stars pulse gently and are joined by a single connecting polyline in accent color.
- Mouse position drives parallax offset for both star layers (background stars move more than the foreground constellation, using each star's own `depth` value) — a real depth illusion, not a single flat pan.
- Click hit-testing is done against the canvas-space coordinates cached from the last draw call, not a separate DOM overlay.
- `prefers-reduced-motion` freezes the twinkle/pulse animation and renders one static frame.

## Components

- **canvas-sky** — the full starfield + constellation renderer.
- **project-star** — a clickable canvas point with a label and fabricated coordinate.
- **plate** — static catalogue-style summary card below the fold, one per project, numbered by Greek letter to match its star.

## Do's and Don'ts

### Do
- Keep constellation lines thin (1px) and low-opacity — they should read as a chart annotation, not a UI connector.
- Use real depth-scaled parallax (background stars drift more than labeled stars) rather than a single flat offset.
- Give every project star a plausible fabricated coordinate — it sells the atlas conceit.

### Don't
- Don't introduce a monospace or technical-looking readout anywhere — it breaks the print-atlas illusion.
- Don't default to a neon/sci-fi palette — the reference is a 19th-century engraved star chart, not a video game.
- Don't skip the click hit-test tolerance (~16px) — canvas stars are small and need forgiving click targets.
