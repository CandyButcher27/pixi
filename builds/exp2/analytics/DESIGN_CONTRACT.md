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
- `max_radius <= 24` — geometry stays inside the reference range (from near:posthog-nemotron-ultra+outlier:live:www.peppasauce.love)

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

## Brief-specific decisions (added — these only add constraints)

- **Product**: Quarry — per-endpoint, per-query cost and latency analytics for backend services. Message: "Every slow request has a line number."
- **Typefaces**: display `Bricolage Grotesque` (800, tight tracking, 112px hero / 16px body = 7.0 dominance); body `IBM Plex Sans`; data and code `IBM Plex Mono`. Fallback stacks end in bare `sans-serif` / `monospace` only — no Inter, system-ui, Arial, Roboto, Helvetica anywhere in the stack.
- **Palette**: paper `#f3f0e8`, ink `#16150f`, rule `#c9c3b3`, signal `#d4420c` (latency over budget), ok `#2f6b3a`. One full-bleed ink band (`#16150f` on paper). Flat fills only.
- **Geometry**: controls and panels radius 2px. Hierarchy from size/weight/rules, not containers — no shadows, no boxed tiles.
- **Section order and anchor side** (text centroid):
  1. Hero — LEFT. Display headline spans ~65% on the left; the right ~30% is a ruled live-tail of slow requests (mono), so the vacated side carries data, not margin.
  2. "Slowest endpoints" — RIGHT, full-bleed ink band. Right-aligned heading + ruled table on the right (numbers first, endpoint and cause last, right-aligned so the column reads as a log tail); left side holds the three-line install snippet.
  3. "How it works" — LEFT. Numbered ordered sequence (huge numerals, running text) in the left 62%; right column carries one large pull figure ("3 lines").
  4. "Pricing" — RIGHT. Ruled price table on the right; left holds the display figure "$0.18 per million spans".
  5. Closing CTA + footer — LEFT, single ruled line.
- **Mandate realisation**: full_bleed via section 2's ink band; centroid_flips via L-R-L-R ordering (4 flips target, >=2 required); display_dominance via 112px hero; largest_card_row via tables/ordered lists (no equal sibling boxes); max_radius 2px.
- **Added constraint**: no row of three or more equal-width siblings anywhere, boxed or not.
