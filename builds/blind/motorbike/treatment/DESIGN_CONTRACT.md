# DESIGN CONTRACT — electric motorbike maker

Direction: medium-density, typography-dominant, absent imagery, rounded geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are discord for fit, hp for contrast, live:www.peppasauce.love for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `discord` — centered hero, uniform rhythm, high card use, rounded geometry, absent imagery, display dominance 10.0
- **contrast** `hp` — right hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 4.5
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:hp)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `display_dominance <= 14.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split >= 0.58` — hero_alignment is right in the references (from contrast:hp)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:discord+contrast:hp)
- `elements_per_1k >= 28` — density is medium in the references (from near:discord+contrast:hp)
- `elements_per_1k < 55` — density is medium in the references (from near:discord+contrast:hp)
- `max_radius >= 20` — geometry is rounded in the references (from near:discord+outlier:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from near:discord+outlier:live:www.peppasauce.love)

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

## Brief-specific decisions (added, do not weaken anything above)

- **Brand**: Varro Motor Works, a small electric motorcycle maker. Three models: Strand (naked roadster), Coil (scrambler), Tern (commuter). Copy is about range, torque and silence, stated as measured numbers, never adjectives.
- **Display face**: Big Shoulders Display 800, condensed, timing-board feel. Never Inter / system-ui / Roboto / Arial / Helvetica in any stack.
- **Body face**: Instrument Sans 400/600. **Figures**: JetBrains Mono for spec readouts.
- **Palette**: bone `#ECE6DA` page, ink `#15130F` text and the full-bleed band, copper `#B4532A` single accent, stone `#D8D0C1` secondary panel. Flat fills only, no gradients, no blur.
- **Geometry**: one radius system. Panels 28px, controls 18px on 60px-tall buttons (well under pill), inputs 14px. Every large surface is rounded, not one panel.
- **Display scale**: body 16px; largest display 160px (ratio 10), section heads 96-112px. Hierarchy is size and weight only; no borders or shadows on panels.
- **Section order and anchor side** (centroid alternates right / left / right / left / right):
  1. Hero, anchor right: headline + copy + CTAs in the right 55%; the left side holds a copper panel with the range figure "212 km" and its test condition, so the vacated side has weight.
  2. Machine, anchor left: long-form copy and a spec list left; right side an ink panel carrying "3.1 s" 0-100 with its conditions.
  3. Range band, full-bleed ink, anchor right: the model lineup as a typographic table on the right; left a large "03" index plus one line.
  4. Charging, anchor left: text and an interactive daily-distance slider that computes charges per week; right side a stone panel with a three-step charge timeline.
  5. Test ride, anchor right: booking form on the right; left a short list of demo cities.
- **Imagery**: none. No photos, no illustrations; figures and type do the work.
- **Density**: medium, roughly 30-50 rendered elements per 1000px of page height.
