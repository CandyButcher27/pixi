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
- `display_dominance <= 19.2` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:agenticos)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:agenticos)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:www.coffeesupreme.com+outlier:live:www.peppasauce.love)
- `max_radius <= 5` — geometry is sharp in the references (from contrast:live:www.coffeesupreme.com)

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

## Brief-specific decisions (added — Torra Marvila, roaster in Lisbon)

Note on direction: the direction line says "dominant imagery", but the inherited mandate `imagery_ratio < 0.06` wins. The page carries no photography; the roaster's material is carried by type, numbers and ruled data instead.

### Typefaces
- Display: **Fraunces** (variable, opsz 144, weight 800, italics for emphasis). Fallback stack `Georgia, serif` only — no generic sans in the display stack.
- Body/data: **IBM Plex Mono** for numbers, tables, labels; **Newsreader** for running text.
- Body size 16px; display 136px (dominance 8.5, inside 6.0–19.2).

### Palette
- Calçada limestone `#EEE7D8` (page), ink `#1B1714`, azulejo cobalt `#1D3A9B` (rules, links, accent), roast `#3A2016` (the full-bleed roastery band, text on it `#EEE7D8`), and a single tram-yellow `#E8B21C` used only for the live roast marker.
- No gradients, no shadows, no backdrop blur. Radius 0 everywhere (added: stricter than `max_radius <= 5`).

### Section order and anchor side (added: hero centroid <= 0.38; every later section's text centroid at least 0.06 off centre, sides alternating)
1. **Hero — LEFT.** 8/4 grid. Left: display headline, lede paragraph, two square-cornered controls. Right (weight of its own): "Na torra hoje" roast log — ruled rows with batch no., origin, charge temp, drop time. Shorter text mass than the left so the centroid stays left.
2. **Lotes actuais — RIGHT.** 3/9 grid. Left: section number and heading. Right: full ruled table of seven current lots (origin, producer, process, altitude, cupping notes, score, 250g price).
3. **A torrefação — LEFT, full-bleed roast-brown band.** Running text on the roasting method and the 1962 Probat UG15 in Marvila, with a roast-curve table; right column is a short spec list.
4. **Assinatura — RIGHT.** Left: heading + one-line terms. Right: subscription plans as ruled rows (not cards), with cadence, quantity, price, delivery zone.
5. **Visita — LEFT.** Café at the roastery: address, opening hours table, transit (tram 28 does not go there — bus 728 does), wholesale contact; right: small shipping/wholesale notes.
6. Footer: dense colophon in mono.

### Mandate realisation
- `full_bleed_sections`: every section spans the viewport with its own background; section 3 is the visibly different roast band.
- `centroid_flips >= 2`: sections alternate L/R/L/R/L by placing the long-text column on alternating sides; the short side holds a heading/numeral/spec list, never empty margin.
- `display_dominance`: one 136px Fraunces headline; section heads 56–72px; no card chrome anywhere.
- `largest_card_row <= 2`: all multi-item information is tables or vertically stacked ruled rows; no equal-width boxed siblings. Added: no grid of 3+ equal boxed items anywhere.
- `imagery_ratio`: no img/video/canvas/background-image url. One inline SVG tile mark only.
- `elements_per_1k >= 55`: dense tables and labelled data rows.
- Controls are rectangular, 0 radius (no pills).
