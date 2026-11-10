# DESIGN CONTRACT — crypto exchange

Direction: high-density, typography-dominant, absent imagery, rounded geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.
- Read as one system, the references are kraken for fit, coinbase for contrast, live:www.peppasauce.love for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `kraken` — left hero, uniform rhythm, high card use, rounded geometry, absent imagery, display dominance 4.5
- **contrast** `coinbase` — centered hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 5.0
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:coinbase)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:kraken)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:kraken+contrast:coinbase)
- `elements_per_1k >= 55` — density is high in the references (from contrast:coinbase+outlier:live:www.peppasauce.love)
- `max_radius >= 20` — geometry is rounded in the references (from near:kraken+outlier:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from near:kraken+outlier:live:www.peppasauce.love)

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

## Brief-specific decisions (added — binding for this build)

Product: **Spreadhouse**, a spot + perps exchange for people who read order books. Message: fees, depth, custody and API limits stated as numbers, not adjectives.

Typefaces
- Display: Bricolage Grotesque 700/800 (hero at 112px on a 16px body = dominance 7.0; secondary display 64px).
- Body: IBM Plex Sans 400/500, 16px.
- Figures: IBM Plex Mono, tabular, used for every price, fee and limit.

Palette (flat colour only, no gradients, no blur)
- paper `#f2efe6`, ink `#15140f`, rule `#d6d0bf`, muted `#6b665a`
- signal `#e8501c` (one accent: CTAs and the live dot), up `#0b7a4b`, down `#b8321f`
- The markets band inverts to ink background, paper text.

Section order and anchor side (each section is asymmetric; the lighter side carries real data, never blank margin)
1. Hero — LEFT: 112px headline, dense lede, figure row; narrow live order-book panel on the right.
2. Markets — RIGHT, full-bleed ink band: wide live markets table on the right, narrow column of filters and session stats on the left.
3. Fees — LEFT: fee schedule table by 30-day volume on the left, narrow worked example on the right.
4. Custody — RIGHT: wide proof-of-reserves ledger panel on the left, attestation method notes (the text-heavy side) on the right; measured centroid 0.62.
5. API — LEFT: code sample panel on the left, endpoints and rate limits table on the right; measured centroid 0.40.
6. Footer: dense link columns + legal.

Added constraints
- Every panel that has a background or border uses radius 24px (no single showcase panel); controls use radius 10px on 46px height (never pill).
- No `<img>`, `<canvas>` or video; sparklines are inline SVG strokes only.
- No three-equal-card rows; hierarchy comes from type size and rules.
- Hero text centroid must measure <= 0.42; section centroids must alternate L/R/L/R/L.
