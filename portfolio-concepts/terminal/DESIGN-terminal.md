---
version: alpha
name: Terminal-OS-portfolio
description: A portfolio that boots like a fake operating system and is navigated entirely by typed commands. An amber-phosphor palette (not the generic matrix green) plays a boot sequence with progress checks, then hands control to a real input line — help, whoami, ls, cat <file>, open <file>, theme, history, clear, and a couple of easter eggs.

colors:
  bg: "#16130F"
  bg-win: "#1C1812"
  bg-elevated: "#241F17"
  ink: "#F4EDE0"
  dim: "#8A8072"
  accent: "#FFB000"
  accent-dim: "#8C6416"
  danger: "#E85C33"
  ok: "#8FBF5E"
  border: "#3A3226"
  bg-light: "#EDE6D3"
  ink-light: "#221D14"
  accent-light: "#A66A00"

typography:
  all:
    fontFamily: "ui-monospace, JetBrains Mono, SF Mono, Consolas, Cascadia Code, monospace"
    use: "Every element on the page — the terminal conceit only works if there is no non-monospace text anywhere"

spacing:
  window-max: 920px
  window-height: 640px
  screen-pad: "20px 22px"

components:
  chrome-bar:
    description: "Fake window titlebar with traffic-light dots and a centered path label — signals 'this is an app', not a page"
  boot-sequence:
    description: "ASCII logo + timed [OK] checklist lines, played once on load before the prompt appears"
  command-line:
    description: "Real text input, invisible/transparent, mirrored into a styled span with a blinking block cursor; supports history (↑/↓) and Tab-complete"
  project-card:
    description: "Boxed output block printed by cat/open/projects — title, year, description, stack, live link"
---

## Overview

Terminal OS treats the portfolio as a machine you log into rather than a page you scroll. On load it plays a short, fake boot sequence (ASCII logo, timed `[OK]` checks) before handing control to a real, working command line — typed input, command history via arrow keys, Tab-completion, and a fixed vocabulary of commands (`help`, `whoami`, `about`, `skills`, `ls`, `projects`, `cat <file>`, `open <file>`, `contact`, `theme [dark|light]`, `history`, `clear`, plus `sudo` and `date` as jokes).

The deliberate departure from the obvious version of this idea: no matrix green. Amber phosphor (`#FFB000` on warm near-black) reads as an *old terminal*, not a hacker-movie prop, and the light theme is a genuine paper-terminal flip (cream ground, dark amber-brown ink) rather than a simple invert.

## Colors

- **Accent** (`#FFB000` dark / `#A66A00` light): prompt tag, command echoes, links, the entire visual language of "this is active."
- **Danger** (`#E85C33`) / **Ok** (`#8FBF5E`): reserved for command feedback only — `command not found`, `sudo` refusal, boot-check `[OK]` — never used decoratively.
- Warm near-black ground (`#16130F`), not pure black — keeps the amber from looking sterile.

## Typography

Monospace, full stop, everywhere. No secondary "body" typeface — a terminal that switches fonts mid-sentence breaks its own premise. Weight and color carry hierarchy instead of a second face.

## Layout & Motion

- Fixed-size "window" (max 920×640) centered in the viewport, with a fake three-dot titlebar — reads as an application, not a webpage.
- Boot sequence: ASCII logo prints instantly, then each check line waits ~180ms before flipping to `[OK]`.
- Scanline overlay via a very low-opacity repeating gradient, blended with `mix-blend-mode: overlay` — atmosphere, not a gimmick users have to fight to read through.
- Input line uses a real `<input>` (opacity 0, positioned over a mirrored `<span>` + blinking `<i>` cursor) so keyboard behavior (selection, IME, mobile keyboards) stays native.

## Components

- **chrome-bar** — traffic lights + centered `jordan@voss: ~/portfolio` label.
- **boot-sequence** — logo + checklist, plays once, then calls `focusInput()`.
- **command-line** — real input, history array with ↑/↓ navigation, Tab-complete against a fixed command list.
- **project-card** — printed by `cat`/`open`/`projects`, boxed output with title/year/description/stack/link.

## Do's and Don'ts

### Do
- Keep every command's output inside the scrollback log (never clear silently except on `clear`).
- Make `open <file>` actually open the link in a new tab — the terminal should do real things, not just print text.
- Respect `prefers-reduced-motion` by skipping the boot-sequence timers (render instantly).

### Don't
- Don't introduce a second typeface "for readability" — it undercuts the whole conceit.
- Don't use matrix green or a glowing CRT-green palette — it's the first thing anyone expects from this idea.
- Don't let unknown commands fail silently — always print a `command not found` line pointing at `help`.
