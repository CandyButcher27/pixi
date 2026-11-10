# DESIGN CONTRACT — kids coding school

Direction: high-density, typography-dominant, absent imagery, rounded geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `mistral.ai` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 5.25
- **contrast** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **outlier** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.peppasauce.love)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from contrast:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `display_dominance <= 17.3` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:mistral.ai)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:mistral.ai)
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

## Brief-specific decisions (added — these only add to the above)

**Product.** Bracket Club, a Saturday and after-school coding school for ages 7 to 15 in Leeds. The page sells by being specific: an age ladder, a minute-by-minute Saturday, real student projects, fees in a table. No three-word value props.

**Typefaces.**
- Display: Bricolage Grotesque 800, tight tracking (-0.04em). Not a generic default.
- Body: Atkinson Hyperlegible 400/700 (designed for legibility, fits a kids/parents audience).
- Code and data: JetBrains Mono 500, used for times, ages, prices, file names.

**Palette (flat, no gradients).**
- Paper `#f4efe4` (page), Ink `#1b1916` (text and the full-bleed band), Tomato `#e5482c` (primary action, highlights), Mustard `#f1b42f` (age-tier markers), Chalk `#fbf8f1` (rounded panels), Rule `#d8d0bf` (hairlines).

**Section order and how each mandate is realised.**
1. Hero — text mass left (h1 + long paragraph + facts list); right column is a rounded "This Saturday" panel with a short timetable. Satisfies `hero_weight_split <= 0.42` and `hero_asymmetry >= 0.08` with a filled right side, not empty margin.
2. The ladder — full-bleed Ink band (`full_bleed_sections >= 1`). Left: display number "7→15" and a short note plus an age picker. Right: a long ruled table of tiers (age, language, what they build, hours). Anchor flips right.
3. A Saturday, minute by minute — left: ruled timeline with times in mono and detailed copy. Right: display "3h 10m" and a brief caption. Anchor flips left.
4. What students shipped — right: ruled list of projects with student first name, age, stack, one-line description. Left: display "412" and a caption. Anchor flips right.
5. Fees and terms — left: fees table and terms list. Right: display "£14/hr" and the bursary note. Anchor flips left.
6. Questions parents ask — right: dense Q&A list. Left: display "FAQ" heading and contact block. Anchor flips right.
- `centroid_flips >= 2`: realised by the six alternating sections above; every "light" side holds a display number plus caption, never blank.
- `largest_card_row <= 2`: no equal-width boxed rows anywhere. Information is tables, ruled lists and two-column splits of unequal width (5fr / 7fr).
- `display_dominance` 6.0–17.3: body 16px; largest display 136px (8.5x).
- `max_radius` 20–40: all panels (hero panel, table wrappers, sign-up block) use 28px. Controls use 10px radius on 52px height, so no pills.
- `elements_per_1k >= 55`: realised through table cells, mono spans and ruled rows, not decoration.
- `imagery_ratio < 0.06`: no images; the only graphics are type.

**Added constraints.**
- No box-shadows on panels; separation comes from rules and type weight.
- Unequal split columns only (5fr / 7fr or 7fr / 5fr), never 1fr 1fr.
