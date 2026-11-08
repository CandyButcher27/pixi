# DESIGN CONTRACT — experimental electronic music festival

Direction: medium-density, typography-dominant, dominant imagery, rounded geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are live:www.midlife.engineering for fit, live:easound.no for contrast, live:superlocaldesign.com for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:www.midlife.engineering` — right hero, uniform rhythm, none card use, pill geometry, absent imagery, display dominance 21.92
- **contrast** `live:easound.no` — unknown hero, uniform rhythm, none card use, rounded geometry, dominant imagery, display dominance 4.5
- **outlier** `live:superlocaldesign.com` — left hero, uniform rhythm, high card use, pill geometry, present imagery, display dominance 7.5

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:easound.no)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from near:live:www.midlife.engineering)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:www.midlife.engineering+contrast:live:easound.no)
- `max_radius <= 24` — geometry stays inside the reference range (from contrast:live:easound.no)

## Prohibitions (inherited — may not be weakened)

- `gradients <= 0` — gradient backdrops are the loudest AI tell (from slop_law)
- `pill_controls <= 0` — fully rounded pill CTAs (from slop_law)
- `glass_panels <= 0` — glassmorphism panels (from slop_law)
- `generic_display_font == False` — Inter / system-ui defaults on the display face (from slop_law)
- `hero_asymmetry >= 0.08` — centred hero column is the default AI composition (from slop_law)

## Yours to decide

- product message, section order, and copy
- the exact display and body typefaces (must not be a generic default)
- the palette, within the direction above
- how each composition mandate is realised structurally

> You may add constraints. You may not weaken or drop an inherited one.

## Brief-specific decisions (mine — additive only)

- **Product**: SIGNAL DECAY 07 — three nights of unstable, generative and broken-machine music in Gemaal Zuid, a decommissioned pumping station in Rotterdam, 19–21 March 2027.
- **Typefaces**: display `Bricolage Grotesque` 800 (variable optical size, squeezed tracking); body `Instrument Sans`; data/timetable `IBM Plex Mono`. No Inter/system-ui anywhere.
- **Palette**: concrete paper `#E9E6DD`, ink `#111110`, signal vermilion `#FF4317` (single accent, flat — never a gradient), deep night `#0C0D0C` for the full-bleed band, rule grey `#B9B4A6`.
- **Geometry**: radius 0 on surfaces, 3px on controls and canvases (cap 24 never approached). Controls are square-shouldered rectangles.
- **Section order (uniform rhythm: every section `padding-block: 120px`)**:
  1. Hero — asymmetric 7/5 grid. Left: wordmark `SIGNAL / DECAY` at ~190px, dates, venue, ticket CTA. Right: tall live canvas (oscilloscope Lissajous) as the imagery. Text mass sits left → hero asymmetry.
  2. Statement — one large running paragraph at display scale (left 8 cols), marginal notes (right 4 cols).
  3. Lineup — three nights as ruled rows; artist names typeset at sizes proportional to billing, set time + room + origin in mono. No cards.
  4. Full-bleed band — edge-to-edge canvas spectrogram on night black, caption overlaid. This is `full_bleed_sections >= 1`.
  5. Rooms — three rooms as alternating rows (canvas image | text, then text | canvas). Each row has two unequal children, both filled; never three across.
  6. Tickets — ruled table rows (tier, what it includes, price, action).
  7. Practical — definition list in ruled rows.
  8. Footer — giant numeral `07` + colophon.
- **Mandate realisation**:
  - `display_dominance >= 6.0`: hero wordmark ~190px vs 17px body (~11x); section heads 64–96px.
  - `largest_card_row <= 2`: all information is vertical sequences of ruled rows; only 2-column splits exist.
  - `full_bleed_sections >= 1`: section 4 is 100vw with an opaque background and a canvas.
  - `max_radius <= 24`: 3px max.
  - Imagery dominance (direction): generative canvases in hero, band, and rooms — target media share >= 0.30.
- **Added constraints**: no marquees, no testimonial strip, no icon grids; motion honours `prefers-reduced-motion`.
