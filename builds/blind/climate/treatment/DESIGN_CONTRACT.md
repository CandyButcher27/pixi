# DESIGN CONTRACT — nonprofit climate campaign

Direction: high-density, typography-dominant, absent imagery, rounded geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `nike` — left hero, uniform rhythm, none card use, pill geometry, absent imagery, display dominance 6.0
- **contrast** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **outlier** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.peppasauce.love)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from contrast:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:nike+contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `display_dominance <= 17.3` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:nike)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:nike)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `max_radius >= 20` — geometry is rounded in the references (from contrast:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from contrast:live:www.peppasauce.love)

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

## Brief-specific decisions (added)

**Campaign.** "No Permit for Bayline": a coalition of 41 groups fighting a proposed LNG export terminal on a tidal estuary. The page is a campaign dossier: the numbers, the timeline to the permit vote, the demands, the money, and one action (sign the public comment).

**Typefaces.** Display: Bricolage Grotesque (700–800, tight tracking). Body and data: Newsreader (serif, running text) + IBM Plex Mono for figures, dates and ledger columns. No Inter / system-ui / Arial / Helvetica anywhere in any font stack.

**Palette.** Paper `#efe9dc`, ink `#16201b`, estuary green `#1f4a3a` (the full-bleed band), tide `#cfe0d4`, signal `#e2502a` (deadlines and the one action only). Flat fills, no gradients, no shadows, no blur.

**Geometry (added constraint).** Rounding is the system, not one panel: every surface (comment panel, ledger blocks, inputs, buttons, the band's inner panels) uses radius 14–28px. Buttons are 12px radius on ~54px height, never pills. max radius stays 28.

**Section order and anchor side** (centroid alternates, and the vacated side always carries content):
1. Hero — LEFT. Headline + dense lead + two actions on the left 60%; right 40% holds the countdown to the permit vote as a giant numeral with a short ruled fact list under it (not empty margin, but low character count so the text mass stays left).
2. The case in figures — RIGHT. Narrow left column: section label and one-sentence thesis; wide right column: a ruled ledger table (metric / figure / source), ~12 rows.
3. Timeline to the vote — LEFT. Wide left column: dated ordered list of hearings and filings; narrow right: the single biggest number (tonnes CO2e/yr) set large, with its derivation.
4. Demands — RIGHT, full-bleed estuary-green band. Left: oversized "Four demands" heading stacked; right: numbered demands as running text with specifics.
5. Sign the comment — LEFT. Form panel (rounded 28) on the left, right side: where the money goes ledger (no equal boxes).
6. Footer — dense colophon, coalition member list as running text.

**Mandate realisation.**
- display_dominance: body 16px, hero h1 ~132px (8.3x), countdown numeral ≤ 240px (≤ 15x). Stays inside 6.0–17.3.
- largest_card_row <= 2: no equal-width bordered sibling rows; all multi-column grids use unequal tracks; tables are rows, not boxes.
- imagery_ratio < 0.06: no images, no canvas, no background-image.
- elements_per_1k >= 55: ledgers, timeline and member list are real granular markup (rows, cells, dates), not filler.
- hero_weight_split <= 0.42 and hero asymmetry: hero text mass sits in the left 60%.
