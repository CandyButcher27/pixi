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
- `display_dominance <= 10.5` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split >= 0.58` — hero_alignment is right in the references (from near:live:www.midlife.engineering)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:live:www.midlife.engineering)
- `elements_per_1k >= 55` — density is high in the references (from near:live:www.midlife.engineering+outlier:live:superlocaldesign.com)
- `max_radius >= 20` — geometry is rounded in the references (from contrast:live:easound.no)
- `max_radius <= 40` — geometry is rounded in the references (from contrast:live:easound.no)

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

**Product.** LOWFORM — four nights of experimental electronic music in a decommissioned
heat plant, Tallinn, 13–16 May 2027. The page is a programme, not an advert: it reads
like a printed festival timetable.

**Typefaces.** Display: Big Shoulders Display 800 (condensed industrial grotesque, lets a
very large size fit a half-width column). Body: Instrument Sans 400/500. Metadata,
times and indices: IBM Plex Mono 400. No Inter / system-ui / Arial anywhere in the
stacks; fallback is the bare `sans-serif` / `monospace` keyword.

**Palette.** Concrete paper `#e7e3da` ground, ink `#141412`, one signal colour
`#ff4a1c` (sodium orange) used only for live/now markers, the ticket price that matters,
and the full-bleed band rule lines. Secondary ink `#5e5b54` for metadata. Flat fills only.

**Section order.**
1. Header — wordmark left, mono nav right, single ticket link.
2. Hero — right-weighted (see below).
3. Statement — one running paragraph at ~34px, set as prose, with a mono margin note.
4. Programme — four nights as ruled timetable rows (time / artist / origin / format / room).
5. Rooms — full-bleed ink band; the three rooms as a numbered sequence with capacity,
   system and character in running text.
6. Passes — ruled price table inside one rounded panel (the only container on the page).
7. Practical — two-column definition list (travel, access, sound policy, age, stay).
8. Footer — colophon in mono.

**How each mandate is realised.**
- `hero_weight_split >= 0.58` / `hero_asymmetry >= 0.08`: hero is a 12-column grid; a
  narrow mono index (dates, coordinates, edition no.) sits in columns 1–3, the title,
  dek and actions occupy columns 6–12. The left column is content, not empty margin.
- `display_dominance` 6–10.5: body 16px, hero title 148px (ratio 9.25). Section heads
  are 64–72px, so hierarchy is carried by type scale, not by boxes.
- `largest_card_row <= 2`: no card grids. Programme, rooms, passes and practical info are
  all vertical sequences of ruled rows; the widest side-by-side arrangement is 2 columns.
- `full_bleed_sections >= 1`: the Rooms band spans 100vw with an ink fill.
- `imagery_ratio < 0.06`: no photos, no canvas, no background images. The only graphic
  is a thin inline-SVG signal trace in the hero index column.
- `elements_per_1k >= 55`: density comes from the timetable — every row splits into
  five measured cells, every night carries 7–8 sets.
- `max_radius` 20–40: the Passes panel has a 28px radius; buttons use 6px radius on a
  52px height (never pill).
- No gradients, no blur, no shadows.

**Added constraints.** No marquee/ticker. No centred section headings. No icon sets.
