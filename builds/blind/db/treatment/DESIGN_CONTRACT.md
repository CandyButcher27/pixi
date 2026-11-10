# DESIGN CONTRACT — open source database

Direction: high-density, typography-dominant, absent imagery, soft geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are supabase for fit, clickhouse for contrast, live:www.peppasauce.love for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `supabase` — centered hero, alternating rhythm, high card use, soft geometry, absent imagery, display dominance 4.0
- **contrast** `clickhouse` — left hero, uniform rhythm, high card use, soft geometry, absent imagery, display dominance 4.5
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:clickhouse)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from contrast:clickhouse)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:supabase+contrast:clickhouse)
- `elements_per_1k >= 55` — density is high in the references (from near:supabase+outlier:live:www.peppasauce.love)
- `max_radius >= 6` — geometry is soft in the references (from near:supabase+contrast:clickhouse)
- `max_radius <= 19` — geometry is soft in the references (from near:supabase+contrast:clickhouse)

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

## Brief-specific decisions (mine; additive only)

Product: **Basalt**, an Apache-2.0, Postgres-wire-compatible database that keeps row and columnar storage in one engine. Audience: backend engineers who read changelogs before landing pages.

Typefaces
- Display: Bricolage Grotesque 800, tight tracking (-0.045em). Hero headline 112px on a 16px body = display dominance 7.0 (inside 6.0..8.0). Section headings 56-64px, never above the hero.
- Body: IBM Plex Sans 400/500. Code, numbers, tables: IBM Plex Mono.
- No Inter / system-ui / Roboto / Arial anywhere in a font stack.

Palette (no gradients, flat fills only)
- Paper #f1ede4, ink #17150f, rule #cfc8b8, muted #6b6558.
- Accent: basalt red #c8401a (links, one CTA fill, syntax keywords). Second accent: lichen #4d6b3c (diff +, passing marks).
- Full-bleed band: ink #17150f with paper text.

Geometry
- Controls radius 6px (44px tall, never pill). Panels/code blocks radius 10px. Nothing above 12px. Hierarchy comes from size and weight, panels are hairline-ruled not shadowed.

Section order and how each mandate is realised
1. Hero, left-weighted (hero_weight_split target ~0.33): headline + lede occupy the left 8/12 columns; the right 4 columns carry a dense install block and a spec list (wire protocol, storage, licence, latest release) so the right side has weight, not margin.
2. "One query, both engines" - RIGHT-weighted: a narrow left rail of numbered notes; the right 8 columns hold a syntax-coloured SQL session with EXPLAIN output.
3. Benchmarks - FULL-BLEED ink band, LEFT-weighted: huge mono figures and the heading left; a narrow right column states method, hardware, and a link to the reproducible harness.
4. Internals - RIGHT-weighted: a short left column with the heading; a dense right-side definition list (storage, WAL, MVCC, replication, extensions) set as ruled rows, not cards.
5. Community / release log - LEFT-weighted: changelog entries on the left; right column carries contributor counts and the licence.
6. Footer: dense link columns.
=> centroids alternate L/R/L/R/L, giving 4 flips (>= 2), each opposing side filled with real content.

Density: elements_per_1k >= 55 is met with tokenised code spans, table cells, and ruled list rows - information density, not decorative wrappers.
Imagery: none. No img/video/canvas/background images (imagery_ratio ~0).
