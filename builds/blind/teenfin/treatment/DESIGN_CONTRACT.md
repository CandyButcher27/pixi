# DESIGN CONTRACT — fintech app for teenagers

Direction: high-density, typography-dominant, absent imagery, rounded geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `revolut` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 13.75
- **contrast** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **outlier** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.peppasauce.love)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from contrast:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
- `display_dominance <= 19.2` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:revolut)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:revolut)
- `elements_per_1k >= 55` — density is high in the references (from near:revolut+contrast:live:www.peppasauce.love+outlier:live:labs.chaingpt.org)
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

**Product.** Kitty — a debit card + app for 13 to 17 year olds. Teen owns the account; a parent is a "guest" who can top up and see totals but not line items unless the teen shares them. Tone: plain, specific, a bit dry. Real numbers everywhere (fees, limits, interest, ages), no three-word value props.

**Typefaces.** Display: Bricolage Grotesque 800 (condensed optical size, slightly odd — reads young without being cartoonish). Body: Figtree 400/600. Figures and ledgers: JetBrains Mono 500. No fallback in any stack names a generic family from the slop list; fallbacks are `sans-serif` / `monospace` only.

**Palette.** Paper `#F2EDE2` base, ink `#191714`, tomato `#E5432A` as the single accent, mint `#C6E6CF` for positive amounts, plum `#2A1C3B` for the one full-bleed dark band. Flat fills only.

**Section order and anchor side** (centroid must alternate, the light side always carries content):
1. Hero — LEFT. 8/12 headline + intro; right 4/12 is a live "this week" mini-ledger (real rows, not empty margin).
2. Ledger — RIGHT. Left 4/12 is a numbered explainer list; right 8/12 is a full month statement table with round-ups.
3. Pots — LEFT, full-bleed plum band. Savings pots as ruled rows with targets, progress as text + thin bar; right side holds the interest rule in large type.
4. Guests (parents) — RIGHT. Left: short permission matrix label; right: running text and a who-sees-what table.
5. Fees — LEFT. Fee table vs typical bank, left-heavy; right narrow: footnotes.
6. Round-up calculator + FAQ — RIGHT. Small label column left; questions as ruled rows right.
7. Sign-up — LEFT. Huge line + age-gated form row.

**Structural rules added.**
- No row of 3+ equal boxed siblings anywhere. Tables use bottom rules only (no cell borders, no cell fills).
- Rounded geometry is shared: every panel (mini-ledger, statement wrapper, calculator, form) uses radius 24-28px; buttons 14px at 56px height (never pill).
- Display size 120px on 16px body (ratio 7.5). Section heads 56-72px.
- No images, no illustrations; numbers and type are the imagery.
