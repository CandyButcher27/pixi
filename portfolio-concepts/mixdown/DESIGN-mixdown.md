---
version: alpha
name: Mixdown-console-portfolio
description: A portfolio styled as a hardware mixing console. Draggable rotary knobs (vertical-drag control, not click-angle), a live sine-driven VU meter, and a tracklist of projects that "play" on click. Brushed-metal charcoal with a rust-copper accent — vintage studio hardware, not a music-app UI.

colors:
  bg: "#1A1A1D"
  panel: "#232326"
  panel2: "#2B2B2F"
  ink: "#EDEAE3"
  dim: "#8C8A85"
  accent: "#D4622B"
  accent2: "#4A9B8E"
  border: "rgba(237,234,227,0.1)"
  bg-light: "#DDD9D0"
  accent-light: "#B14A1D"

typography:
  display:
    fontFamily: "Arial Narrow, Segoe UI, system-ui, sans-serif"
    weight: 800
    transform: uppercase
    use: "Hero headline, unit labels — condensed industrial equipment lettering"
  body:
    fontFamily: "-apple-system, Segoe UI, system-ui, sans-serif"
    use: "Role line, about paragraph"
  utility:
    fontFamily: "ui-monospace, SF Mono, Consolas, monospace"
    use: "Channel labels, dB-style readouts"

spacing:
  unit-pad: "28px 32px"
  console-gap: 18px

components:
  unit:
    description: "A rack panel — the console's structural unit, houses the hero, the channel strip, and the tracklist"
  knob:
    description: "Rotary control driven by vertical drag distance (not absolute cursor angle); rotation rendered on a real needle child element, conic-gradient fill shows value"
  vu-meter:
    description: "16-bar meter animated continuously via layered sine waves, speed/intensity tied to a master 'Energy' fader"
  track-row:
    description: "Tracklist row (number, name, substack, year, play glyph) — click opens the case-study modal and marks the row 'playing'"
---

## Overview

Mixdown recasts the portfolio as a piece of studio hardware: a rack of panels holding a channel strip (three rotary knobs + a live VU meter), a master energy fader, and a tracklist of projects that behave like tape tracks. The console vocabulary — unit labels, lamp indicators, channel strips — comes from real mixing desks, not generic "audio app" UI chrome.

The rotary knobs are driven by **vertical drag distance**, matching how real DAW/hardware knobs behave, deliberately avoiding the more obvious (and more fragile) approach of computing rotation from the cursor's absolute angle around the knob center — that approach wraps unpredictably near the bottom of the knob and was the exact bug fixed in this build.

## Colors

- **Accent** (`#D4622B` rust-copper): knob fill, active track state, primary interactive color — reads as warm hardware, not a UI-blue.
- **Accent2** (`#4A9B8E` teal): VU meter secondary bars only — creates the two-tone meter look real consoles have, never used for text or links.
- Charcoal ground (`#1A1A1D`) with two elevated panel tones (`#232326`, `#2B2B2F`) gives the rack panels real depth without borders doing all the work.

## Typography

Condensed, heavy, uppercase sans for anything that reads as an equipment label (headline, unit labels, channel names) — mimics silk-screened panel lettering. Regular-weight sans for prose; monospace only where a real console would print numbers (channel labels, dB-style values).

## Layout & Motion

- VU meter bars driven by `requestAnimationFrame`, each bar's height from a phase-offset sine wave scaled by the master "Energy" fader (a real `<input type="range">`), so the meter feels ambient rather than looping visibly.
- Knob rotation: `mousedown` records start Y + start value; `mousemove` computes `(startY - clientY) * 0.5` and clamps 0–100 — smooth, no angle wraparound.
- Tracklist rows open a modal on click and visually mark themselves "playing" (accent-colored) until another row is clicked.
- One knob ("Hue Shift") is wired to actually retint the page's accent color live — the control does something real, not just cosmetic rotation.

## Components

- **unit** — rack panel wrapper with a lamp-indicator label row.
- **knob** — rotary control, vertical-drag-driven, real needle element + conic-gradient value ring.
- **vu-meter** — 16-bar ambient meter, energy-scaled.
- **track-row** — tracklist entry, click opens modal + marks playing state.

## Do's and Don'ts

### Do
- Drive knob rotation by drag *distance*, never by absolute cursor angle around the pivot.
- Keep accent2 confined to the VU meter — it should never appear as a link or button color.
- Let at least one control (Hue Shift) produce a real, visible effect beyond its own rotation.

### Don't
- Don't compute knob angle from `atan2` on live cursor position relative to the knob center — it wraps and jumps near 180°.
- Don't inject per-element `<style>` tags to fake a pseudo-element rotation — give the rotating part (the needle) a real DOM node and set its transform directly.
- Don't let the VU meter freeze under `prefers-reduced-motion` without a static fallback — render bars at a fixed height instead of animating.
