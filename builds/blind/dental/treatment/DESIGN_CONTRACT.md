# DESIGN CONTRACT — dental clinic

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

**Product.** Halden Street Dental, an independent six-chair practice in Leeds (LS6). The page answers what a nervous adult actually checks before booking: what the treatment is, how long it takes, what it costs, who does it, when the next slot is.

**Typefaces.** Display: Bricolage Grotesque 800 (tight tracking, -0.04em). Body: IBM Plex Sans 400/500. Figures, prices, durations and registration numbers: IBM Plex Mono. No Inter, no system-ui as a display face.

**Palette.** Bone paper `#F2EDE3`, ink `#16241F`, deep surgery green `#1F4A3F`, film black `#0E1513` for the x-ray band, signal coral `#E2583A` used only for the next-slot marker and the primary action, pale enamel `#FBF8F2`. Flat fills only — no gradients anywhere, including inside the SVG art.

**Section order and how each mandate is realised.**
1. Hero — text anchored left (headline, live "next slots" ruled list, phone, hours); a large illustrated treatment-room panel fills the right. Hero centroid well left of centre (target < 0.38).
2. Panoramic x-ray band — full-bleed film-black section (the full_bleed mandate). Generated panoramic radiograph illustration occupies the left ~60% to the edge; the right carries a ruled list of what a check-up actually measures. Anchor flips right.
3. Treatments — numbered ruled rows (name, what happens, chair time, from-price) on the left; a labelled tooth cross-section diagram on the right. Anchor flips left.
4. Fees — instruments illustration on the left; the full fee table (private / plan member columns) on the right. Anchor flips right.
5. Clinicians — running-text bios with GDC numbers and specialisms on the left; two portraits of different sizes, offset, on the right (never a row of equal headshot cards). Anchor flips left.
6. Visit & book — street map illustration on the left; booking form, opening hours table, access notes on the right. Anchor flips right.

**Imagery.** All imagery is original inline SVG rendered into `<img>` elements (self-contained, no external assets). Combined image area targets >= 0.33 of the page so imagery_ratio holds with margin. Images sit in panels with 28px radius; that panel radius is the max_radius (20–40 band). Controls use 10px radius on >= 50px-tall buttons, so nothing is pill-shaped.

**Density.** Information lives in ruled rows and tables (slots, readings, treatments, fees, hours), which delivers elements_per_1k >= 55 as content, not decorative spans. No row of three or more equal boxes anywhere; image pairs are deliberately unequal.

**Display scale.** h1 at 9rem on a 16px body (dominance ~9), section heads 4.25rem — inside the 6.0–20.8 band.
