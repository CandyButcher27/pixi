# DESIGN CONTRACT — modern art museum

Direction: high-density, typography-dominant, absent imagery, sharp geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.
- Read as one system, the references are apple for fit, live:www.stedelijk.nl for contrast, cal for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `apple` — centered hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 3.5
- **contrast** `live:www.stedelijk.nl` — right hero, uniform rhythm, low card use, sharp geometry, absent imagery, display dominance 4.73
- **outlier** `cal` — left hero, alternating rhythm, high card use, pill geometry, absent imagery, display dominance 4.0

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.stedelijk.nl)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:cal)
- `display_dominance >= 3.8` — display typography carries the hierarchy instead of card chrome (from contrast:live:www.stedelijk.nl)
- `display_dominance <= 5.8` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split >= 0.58` — hero_alignment is right in the references (from contrast:live:www.stedelijk.nl)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:apple+contrast:live:www.stedelijk.nl+outlier:cal)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:www.stedelijk.nl+outlier:cal)
- `max_radius <= 5` — geometry is sharp in the references (from contrast:live:www.stedelijk.nl)

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

## Brief-specific decisions (added, do not weaken the above)

- **Institution:** Ostkai, a fictional municipal museum of modern and contemporary art on a converted grain quay. Copy is specific: room numbers, dates, prices, holdings counts, opening hours.
- **Typefaces:** display Archivo (variable width, set condensed at wdth 70, weight 800); body Newsreader (serif, 16px); labels and data IBM Plex Mono. No Inter / system-ui anywhere.
- **Palette:** paper #f1eee6, ink #121212, signal vermilion #e2400f, rule grey #b9b4a8. Flat fills only, no gradients, no shadows, no blur.
- **Geometry:** every radius is 0. Controls are rectangular, ruled with 1.5px ink borders.
- **Type scale:** body 16px, display h1 84px (ratio 5.25, inside 3.8-5.8). Nothing else exceeds 84px. Section heads 44-56px.
- **Section order and anchor side** (realises `centroid_flips >= 2`, `hero_weight_split >= 0.58`):
  1. Hero, anchor RIGHT: right-aligned headline + intro fill the wide right column; a 320px ruled "today" index sits at left (open status, current rooms) - real content, not margin.
  2. Now showing, anchor LEFT: dense exhibition ledger (room, title, artists, dates) on the left; on the right a drawn floor plan of the building built from ruled divs, a non-text weight.
  3. Collection in numbers, full-bleed ink band (realises `full_bleed_sections >= 1`), anchor RIGHT: holdings figures and acquisition notes in the right columns, a vertical vermilion bar and section label at left.
  4. Programme, anchor LEFT: week calendar of talks, screenings, workshops; right column a solid vermilion membership panel with short text.
  5. Visit, anchor RIGHT: hours, prices, access, address in a dense table on the right; left carries the large section head.
- **Imagery:** none (`imagery_ratio < 0.06`). The floor plan is the only figure, drawn in CSS borders.
- **Density:** tables, ledgers and lists give > 55 visible elements per 1000px of height.
- **Hero:** asymmetric by construction (320px / 1fr grid, headline set flush right), no centred column.
