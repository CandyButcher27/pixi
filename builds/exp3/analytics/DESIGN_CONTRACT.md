# DESIGN CONTRACT — developer analytics platform for backend engineers

Direction: medium-density, typography-dominant, absent imagery, pill geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are posthog-nemotron-ultra for fit, vercel for contrast, live:www.peppasauce.love for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `posthog-nemotron-ultra` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 3.0
- **contrast** `vercel` — centered hero, alternating rhythm, none card use, pill geometry, absent imagery, display dominance 3.0
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:vercel)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:vercel)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:vercel+outlier:live:www.peppasauce.love)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:posthog-nemotron-ultra)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:posthog-nemotron-ultra+contrast:vercel)
- `elements_per_1k >= 55` — density is high in the references (from near:posthog-nemotron-ultra+outlier:live:www.peppasauce.love)
- `max_radius >= 20` — geometry is rounded in the references (from outlier:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from outlier:live:www.peppasauce.love)

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

## Brief-specific decisions (added — these only add to the inherited constraints)

- **Product**: Spanwise — query-level latency analytics for backend services. Message: "the slow path, ranked", not "insights".
- **Typefaces**: display `Bricolage Grotesque` 700 (hero 112px on a 16px body = 7.0 dominance, inside 6.0–8.0); body `IBM Plex Sans`; data and code `JetBrains Mono`. No fallback stack names a generic default (no Inter, system-ui, Arial, Roboto, Helvetica Neue).
- **Palette**: paper `#F2EFE7`, ink `#15171A`, graphite `#5B5E63`, rule `#CFCABD`, signal oxide `#C2410C` (used only for regressions and the primary action), one full-bleed ink band `#15171A` with paper text. Flat fills only, no gradients, no blur.
- **Geometry**: controls radius 12px on 52px-tall buttons (well under pill threshold); one code/readout panel at radius 28px supplies the rounded geometry (20–40). Nothing else gets chrome.
- **Section order and anchor side** (centroid flips realised by where the dense text sits; the opposite side always holds a display numeral or heading, never empty margin):
  1. Hero — left: 112px headline + lede + actions; right: narrow trace readout (span waterfall as ruled mono rows). Text mass left (split <= 0.42).
  2. "Read the query, not the dashboard" — right: numbered attribution sequence (ruled list) + setup code panel; left: sticky display statistic (11h) with attribution.
  3. "The slow path, ranked" — left: sortable ruled endpoint table (route, p50, p99, calls, time lost, sparkline, delta); right: display numeral (+38% p99) and section heading.
  4. Full-bleed ink band "What it watches" — right: ruled definition list of signals with units; left: display heading.
  5. Pricing as a ruled comparison table (not three cards) — left: table + terms; right: display numeral ($0) and a one-line free-tier promise.
  6. Footer — install line and link columns.
- **Card rows**: no row of three or more equal boxed siblings anywhere; tables and ruled lists carry all repeated information.
- **Imagery**: none. The only graphics are inline SVG sparklines inside table cells.
- **Density**: dense ruled tables and mono rows to keep elements per 1k px >= 55.
