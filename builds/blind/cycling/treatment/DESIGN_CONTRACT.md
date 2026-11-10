# DESIGN CONTRACT — cycling apparel brand

Direction: medium-density, typography-dominant, absent imagery, soft geometry, alternating section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.
- Read as one system, the references are airtable for fit, supabase for contrast, mastercard for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `airtable` — left hero, alternating rhythm, high card use, pill geometry, absent imagery, display dominance 2.81
- **contrast** `supabase` — centered hero, alternating rhythm, high card use, soft geometry, absent imagery, display dominance 4.0
- **outlier** `mastercard` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 8.0

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:supabase)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:supabase)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:mastercard)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:airtable+outlier:mastercard)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:airtable+contrast:supabase+outlier:mastercard)
- `elements_per_1k >= 28` — density is medium in the references (from near:airtable+outlier:mastercard)
- `elements_per_1k < 55` — density is medium in the references (from near:airtable+outlier:mastercard)
- `max_radius >= 6` — geometry is soft in the references (from contrast:supabase)
- `max_radius <= 19` — geometry is soft in the references (from contrast:supabase)

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

## Brief-specific decisions (added — additive only)

- **Brand**: Échappée — cycling garments built for long, early, cold rides. The message is the garment's numbers: grams, GSM, seam counts, temperature windows, repair terms.
- **Typefaces**: display `Big Shoulders Display` 800 (condensed, race-number heritage); body `Hanken Grotesk` 16px; numerals and specs `JetBrains Mono`. No fallback list may name Inter, Roboto, Arial, Helvetica Neue, system-ui or Segoe UI.
- **Display scale**: one hero headline at 112px over 16px body (dominance 7.0, inside 6.0–8.0). Section headings 64px; no other text above 64px. Hierarchy comes from size/weight/tracking, not boxes: no box-shadows anywhere.
- **Palette**: paper `#EEEAE1`, ink `#17191A`, road-oxide red `#B8361E` (accent, used for numerals and the primary control only), forest `#1E3A2D` for the full-bleed fabric section with paper text. Flat fills only, zero gradients.
- **Geometry**: controls radius 8px, spec panels radius 12px (max_radius 12, inside 6–19). Controls are 48px tall, so no pill.
- **Imagery**: none raster. One inline SVG elevation profile (stroke only) is the only graphic; it is data, not decoration.
- **Section order and anchor side** (realises `centroid_flips >= 2` with the far side always carrying data):
  1. Hero — LEFT: headline + lede across 8 columns; right 4 columns hold the season ledger (piece count, weights, ride hours tested).
  2. The kit — RIGHT: heading and 6-piece numbered list on the right 7 columns; left 5 columns hold the elevation SVG of the test loop with mono stats.
  3. Fabric lab — LEFT, FULL BLEED forest band: heading + fabric table left; right column carries temperature-window scale.
  4. Fit by discipline — RIGHT: heading + three-discipline spec table on the right; left carries the size chart lookup.
  5. Repair, forever — LEFT: heading + terms; right carries repair counts.
- **Density**: medium (28–55 elements per 1000px) via spec tables and ledgers, not card grids. No row of three equal boxed cards.
- **Hero asymmetry**: hero text centroid kept ≤ 0.42 by weighting the headline into the left 2/3.
