# DESIGN CONTRACT — boutique hotel in Marrakech

Direction: high-density, typography-dominant, dominant imagery, sharp geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:wanderful.index.studio` — right hero, uniform rhythm, low card use, pill geometry, dominant imagery, display dominance 9.23
- **contrast** `live:verana.com` — left hero, uniform rhythm, low card use, sharp geometry, dominant imagery, display dominance 4.17
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:verana.com)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:wanderful.index.studio+contrast:live:verana.com+outlier:live:www.peppasauce.love)
- `display_dominance <= 12.9` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split >= 0.58` — hero_alignment is right in the references (from near:live:wanderful.index.studio)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from near:live:wanderful.index.studio+contrast:live:verana.com)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:verana.com+outlier:live:www.peppasauce.love)
- `max_radius <= 5` — geometry is sharp in the references (from contrast:live:verana.com)

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

## Brief-specific decisions (added — Dar Tilwa, an 11-room riad in Mouassine)

- **Typefaces**: display `Bodoni Moda` (high-contrast didone, italic for the name); body `Newsreader`; figures, times, room data `IBM Plex Mono`. No Inter/system-ui anywhere.
- **Palette** (flat, no gradients): plaster `#EFE3CF`, tadelakt terracotta `#B0502B`, rose wall `#C76A4A`, Majorelle-dark `#24358F`, saffron `#D9A23A`, palm `#3E5B3A`, ink `#1F1712`.
- **Geometry**: every box has `border-radius: 0`. Curves live only inside the illustrations (horseshoe arches), never on UI chrome. CTAs are underlined text links or square-cornered blocks.
- **Imagery**: flat SVG illustrations (courtyard through an arch, Majorelle door, zellige star tile, roof terrace with the Atlas, the kitchen table, medina map) used as `background-image` panels that fill one half of each split section at full section height, plus one full-bleed zellige band. Target ratio >= 0.35.
- **Section order and anchor side** (text side listed; the other side is always a full-height illustration, never empty margin):
  1. Hero — text RIGHT (centroid ~0.75), courtyard-through-arch illustration left. Name at 128px (body 16px, dominance 8.0).
  2. The house — text LEFT, floor-by-floor ruled list; Majorelle door right.
  3. Zellige band — full-bleed, no text.
  4. Rooms — text RIGHT, an 11-row ruled table (room, floor, m², bed, light, from-rate); zellige panel left.
  5. A day in the house — text LEFT, timed schedule; roof terrace right.
  6. Kitchen — text RIGHT, priced menu as ruled rows; table still-life left.
  7. Getting here — text LEFT, distance/time table; medina map right.
  8. Footer — text RIGHT, booking terms and contacts.
- **Hierarchy**: size and weight only. Section heads 64px Bodoni, numbered kickers in Plex Mono 12px uppercase; rows separated by 1px rules, no cards, no shadows.
- **Density**: every section carries real specifics (dimensions, minutes, dirhams, times) — no three-word value props.
