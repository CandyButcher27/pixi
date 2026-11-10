# DESIGN CONTRACT — wedding photographer

Direction: high-density, typography-dominant, dominant imagery, rounded geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **contrast** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38
- **outlier** `live:ohhmydesign.com` — unknown hero, alternating rhythm, high card use, pill geometry, dominant imagery, display dominance 14.88

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:labs.chaingpt.org)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:labs.chaingpt.org)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from near:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:www.peppasauce.love+contrast:live:labs.chaingpt.org)
- `display_dominance <= 20.8` — display scale stays inside the reference range (from median of triple)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from contrast:live:labs.chaingpt.org+outlier:live:ohhmydesign.com)
- `elements_per_1k >= 55` — density is high in the references (from near:live:www.peppasauce.love+contrast:live:labs.chaingpt.org+outlier:live:ohhmydesign.com)
- `max_radius >= 20` — geometry is rounded in the references (from near:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from near:live:www.peppasauce.love)

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

**Concept.** "Mara Ilves — wedding photographs, filed like a contact sheet." A documentary photographer who covers the whole day and records it as a log: frame counts, timestamps, venues, delivery weeks. The page reads like her ledger, not a brochure.

**Typefaces.** Display: Instrument Serif (italic for emphasis). Body: Hanken Grotesk 15px. Metadata (times, frame numbers, prices): JetBrains Mono 12px. No Inter / system-ui anywhere.

**Palette.** Paper `#efe9de`, ink `#1c1915`, oxblood accent `#7b2d21`, rule `#c9bfae`, one dark band `#1c1915` for the index. Flat colours only — no gradients, no blur.

**Geometry.** Every photograph sits in a frame with `border-radius: 28px` and a paper-dark background; the two dark panels share the same 28px radius. Buttons are rectangles with 6px radius (never pill). Max radius stays 28 (inside 20–40).

**Section order and how each mandate is realised.**
1. Hero — headline + running intro + ledger stats on the left (text weight left, ~0.3); a tall framed b&w photograph fills the right side, so the "empty" side carries the image. Display type ~150px over 15px body (ratio ~10, inside 6–20.8).
2. Full-bleed band — one photograph edge to edge (100vw, ~680px), caption column set in the right third (text weight right). Flip 1.
3. "How a day is covered" — a ruled timeline (time / what happens / frames) on the left, a framed candid photograph on the right. Flip 2.
4. Index of recent weddings — a ruled table in the right two thirds; two stacked framed photographs on the left. Flip 3.
5. Collections — three collections as ruled rows with specifics (hours, shooters, frames, weeks, price), not three equal cards; framed photograph on the right. Flip 4.
6. Questions + enquiry — FAQ ruled list and a short form in the right portion; a strip of unequal photographs on the left. Flip 5.
7. A gallery strip of photographs at deliberately unequal widths (never an equal-width row).

**Density.** Tables, timelines and FAQ rows carry the numbers; target well over 55 elements per 1000px.

**Imagery.** Real wedding photographs (`<img>`), framed and rounded, targeting ≥ 0.35 of page area.
