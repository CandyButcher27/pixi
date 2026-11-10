# DESIGN CONTRACT — local bakery

Direction: high-density, typography-dominant, dominant imagery, sharp geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:localstudio.fr` — centered hero, uniform rhythm, none card use, sharp geometry, dominant imagery, display dominance 19.95
- **contrast** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **outlier** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.peppasauce.love)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from contrast:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:localstudio.fr+contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `display_dominance <= 27.9` — display scale stays inside the reference range (from median of triple)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from near:live:localstudio.fr+outlier:live:labs.chaingpt.org)
- `elements_per_1k >= 55` — density is high in the references (from near:live:localstudio.fr+contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `max_radius <= 5` — geometry is sharp in the references (from near:live:localstudio.fr)

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

- **Product**: Lamp Street Bakery, a one-oven neighbourhood bakery. Message: the page is the bake sheet — what comes out of the oven, when, and what it costs.
- **Typefaces**: display `Young Serif` (400); body `Newsreader`; figures, times and prices `IBM Plex Mono`. No Inter, no system-ui anywhere.
- **Palette**: flour `#F2EBDD` ground, ink `#1D1915` text, crust `#A3461D` accent, rye `#4E3221` dark band, butter `#E4C063` highlight. Flat fills only, no gradients (also inside illustrations).
- **Imagery**: flat SVG illustrations (oven, racks, boule, lamination, wheat, shopfront) delivered as `<img>` data URIs, each filling half a section or the full width, so imagery ratio clears 0.3 and the image side of every split is the weight the text leaves.
- **Section order and anchor side** (text centroid): 1 hero, text left / oven image right · 2 full-bleed rack band, text right · 3 daily bake schedule as a ruled timetable, left / boule right · 4 price list as ruled rows, image left / list right · 5 baker's notes running text left / lamination image right · 6 visit + pre-order, shopfront left / hours + form right.
- **Density**: timetable rows (time, loaf, batch size, oven temp), price rows (item, flour, weight, price), hydration figures and dates in mono — no three-word value props.
- **Geometry**: radius 0 everywhere; controls are square-cornered ink blocks; hierarchy comes from type size and rule lines, never shadows or card boxes.
- **No equal-box rows**: lists are vertical ruled rows; the only side-by-side siblings are the asymmetric splits (7/5, 5/7).
