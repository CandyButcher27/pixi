# DESIGN CONTRACT — independent coffee roaster in Lisbon

Direction: high-density, balanced-hierarchy, dominant imagery, sharp geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `agenticos` — left hero, uniform rhythm, none card use, pill geometry, absent imagery, display dominance 13.75
- **contrast** `live:www.coffeesupreme.com` — centered hero, uniform rhythm, none card use, sharp geometry, dominant imagery, display dominance 2.5
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.coffeesupreme.com)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:agenticos+contrast:live:www.coffeesupreme.com+outlier:live:www.peppasauce.love)
- `max_radius <= 24` — geometry stays inside the reference range (from contrast:live:www.coffeesupreme.com+outlier:live:www.peppasauce.love)

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

## Brief-specific decisions (added — these only tighten the inherited contract)

Product: Mosca Torrefação, a one-drum roaster and counter at Rua da Boavista 84, Cais do Sodré. The page sells this week's lots, a roast-to-door subscription, and the counter itself.

Typefaces
- Display: Young Serif (Google Fonts), 400 only. Hero at clamp(5rem, 11vw, 10rem), at least 6x the 17px body, so `display_dominance >= 6.0` holds at desktop widths.
- Body: Newsreader, 17px / 1.55. Data and labels: IBM Plex Mono 13px, uppercase, tracked.
- Fallback stacks use only `Georgia, serif` and `monospace`, so no generic family name appears anywhere in a computed font-family.

Palette (flat colours only, no gradients)
- Cal (lime-wash wall) #f2ede3 as page ground; ink #1c1a16; azulejo cobalt #1d3c8f; roof terracotta #b4532c; cork #d9c7a5 for rules and quiet fills.

Geometry
- Corners 0 everywhere; maximum 2px on inputs. Controls are rectangular, ruled with a 1.5px ink border. No shadows, no backdrop filters.

Section order and how each mandate is realised
1. Hero: left 7/12 carries the display headline, a dense paragraph and a roast-status line; right 5/12 is an azulejo-tile image panel with a stamped lot label. Text centroid sits left (< 0.42), the right side carries weight through imagery, not margin. (`hero_asymmetry`, `centroid_flips` start: L)
2. This week's lots: left 4/12 is a tall tile image column with origin notes; right 8/12 is a ruled table (lot, origin, process, altitude, roast date, notes, price). Anchor right. No cards; information is a table. (`largest_card_row`, flip 1: R)
3. Full-bleed cobalt band, edge to edge, tile pattern as background: a long display quote and the roasting numbers on the left, pattern carrying the right. (`full_bleed_sections`, flip 2: L)
4. How a lot is roasted: left is a roast-curve image (bean temperature vs time); right is a numbered ruled sequence of six steps with temperatures and times. Anchor right. (flip 3: R)
5. Counter and visit: left is address, hours table and what is on the bar; right is a street-plan image of Cais do Sodré. Anchor left. (flip 4: L)
6. Subscription: left a single display numeral block, right the plan rules as a ruled definition list and a rectangular form. Anchor right. (flip 5: R)

Added constraints
- No row of three or more equal-width siblings anywhere, even unboxed.
- Every section states at least one specific number (grams, degrees, metres, euros, days).
- Imagery is drawn in SVG (tile, roast curve, street plan) and placed as image media, never as decoration behind centred text.
