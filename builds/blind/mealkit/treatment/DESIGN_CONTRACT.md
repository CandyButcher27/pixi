# DESIGN CONTRACT — vegan meal kit delivery

Direction: high-density, typography-dominant, absent imagery, rounded geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `uber` — centered hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 3.5
- **contrast** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **outlier** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.peppasauce.love)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from contrast:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `display_dominance <= 17.3` — display scale stays inside the reference range (from median of triple)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:uber)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `max_radius >= 20` — geometry is rounded in the references (from contrast:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from contrast:live:www.peppasauce.love)

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

## Brief-specific decisions (added, nothing above is weakened)

- **Product**: "Furrow" — weekly vegan meal kits, 12 rotating recipes, ingredients from named farms, delivered Tue/Thu.
- **Typefaces**: display `Young Serif` (one weight, set very large, tight leading); body `Public Sans`; figures and data `JetBrains Mono`. No Inter / system-ui anywhere in the display role.
- **Palette**: oat `#f1e9d8` ground, aubergine ink `#2b1226`, chili `#c8401b` accent, leaf `#2f5a36` for the full-bleed band, bone `#fbf7ee` for panels. Flat fills only, no gradients, no blur.
- **Display scale**: hero h1 at 168px over a 16px body (ratio ~10.5, inside 6–17.3).
- **Geometry**: panels radius 28px; buttons radius 10px on 50px-tall controls (never pill). Rows are ruled with 1px rules, not boxed.
- **Section order and anchor side** (each section is a direct child of `main`, so the alternation is measured):
  1. Hero — anchor LEFT: headline + lede + order controls; right column carries this week's box receipt in mono (weight, not margin).
  2. Menu — anchor RIGHT: a 12-row ruled table (recipe, time, kcal, protein, allergens); left carries a large "12" and the cutoff note.
  3. How it works — anchor LEFT, full-bleed leaf band: numbered ordered list of 4 steps with times; right carries a rounded delivery-schedule panel.
  4. Farms — anchor RIGHT: ruled list of 7 farms with crop, county, miles; left carries a large average-distance figure.
  5. Plans — anchor LEFT: pricing as table rows (people x meals) with a live calculator; right carries a short FAQ.
- **Cards**: no row of 3+ equal boxes anywhere; information is rows, lists, tables.
- **Imagery**: none. Hierarchy from type only.
- **Density**: numbers everywhere (minutes, grams, kcal, miles, prices); target well over 55 elements per 1000px.
- **Measured column splits** (set after repair round 1): hero 1.9fr/1fr (centroid 0.39), menu 1.3fr/1.6fr (0.56), how 1.7fr/1fr (0.38), farms 1fr/1.6fr (0.56). The side panels for menu and farms each hold a big display figure (12 recipes, 94 mi) and a short line, so the side the anchor leaves still has something on it.
