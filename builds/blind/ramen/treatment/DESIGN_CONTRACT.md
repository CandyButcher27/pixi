# DESIGN CONTRACT — ramen bar in Osaka

Direction: high-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `mistral.ai` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 5.25
- **contrast** `tesla` — right hero, uniform rhythm, none card use, pill geometry, absent imagery, display dominance 2.84
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:tesla)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:tesla+outlier:live:www.peppasauce.love)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:mistral.ai)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:mistral.ai+contrast:tesla)
- `elements_per_1k >= 55` — density is high in the references (from contrast:tesla+outlier:live:www.peppasauce.love)
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

## Brief-specific decisions (added — do not weaken anything above)

**Concept.** Menya Kuroboshi, an 11-seat counter ramen bar under the tracks at Tenma, Kita-ku, Osaka. The page reads like the board above the counter: menu, broth schedule, house rules, directions — all specifics, prices in yen, times, seat counts.

**Typefaces.** Display: `Dela Gothic One` (heavy Japanese gothic, signage voice). Body: `Zen Kaku Gothic New`. Numerals/labels: `IBM Plex Mono`. Font stacks end in plain `sans-serif` / `monospace` only — no Inter, system-ui, Roboto, Arial, Helvetica in any stack.

**Palette.** Broth cream `#f1e7d3` page, soy black `#1b1512` ink, chashu red `#b8321e` accent, nori green-black `#23302a` for the full-bleed band, tare amber `#c98a2b` for numerals on dark. Flat fills only, no gradients, no blur.

**Section order and how each mandate is realised.**
1. Hero — left-weighted (wide left column: 7.2rem display wordmark + dense paragraph and fact line; right narrow column: rounded 24px "tonight" board with broth status and queue). Centroid target ≈ 0.35. Display 112px over 16px body = 7.0 dominance.
2. Menu — right-weighted: narrow left label column, wide right ruled table of bowls/toppings/drinks. Information is rows, not cards.
3. Broth by the hour — full-bleed nori band (100vw, opaque). Left-weighted: wide timeline of the 18-hour simmer as ruled rows; right column: short numeric facts.
4. Counter rules — right-weighted: left column holds the 11-seat counter map in a rounded panel (seats are small, <120px, not a card row); right wide column holds numbered house rules as running text.
5. Visit — left-weighted: hours table and directions from Tenma station on the left; right rounded panel with ticket-machine notes.
6. Footer.
Flip sequence L R L R L → 4 flips; every "light" side carries real content.

**Geometry.** Panels 24px radius (board, seat map, visit panel) — rounded is a system, not one panel. Controls are rectangles with 6px radius, never pills. Max radius 24 (within 20–40).

**Density.** Tables, ruled lists, mono labels; target ≥ 70 elements per 1000px. No imagery at all (ratio 0).
