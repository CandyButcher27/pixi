# DESIGN CONTRACT — AI writing assistant

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

**Product.** "Marginalia" — an AI writing assistant that edits in the margin instead of
over your sentences. Every suggestion is a marginal note with a reason; the draft stays yours.

**Typefaces.** Display: Gloock (high-contrast editorial serif), 124px hero headline.
Body: Literata 16px (a reading face, built for long screen text). Annotations, labels,
numbers: JetBrains Mono. No Inter / system-ui anywhere, including fallbacks (fallback is `serif` / `monospace`).

**Palette.** Proof paper `#f1ebdd`, ink `#1c1a16`, proofreader's red `#c2391b`,
press-blue `#23466b` for the dark band, rule grey `#cfc5b0`. Flat fills only — no gradients, no blur.

**Section order and anchor side (text centroid must alternate; the opposite side always holds an image):**
1. Hero — text left (headline, 3-line lede, two square-cornered 6px-radius buttons, spec line); manuscript-with-margin-notes image right.
2. "Seven passes" — annotated-page image left; ordered list of the seven editing passes with what each one checks, right.
3. Full-bleed press-blue band — benchmark table (rows of numbers: acceptance rate, edit distance, latency) left; redline-diff image right.
4. "Voice, not template" — style-sheet image left; ruled table of house-style rules it learns, right.
5. Pricing as ruled rows (not cards) left; desk image right.
6. Colophon footer.

**How mandates are realised.**
- full_bleed: section 3 spans 100vw with an opaque background.
- centroid_flips: L, R, L, R, L across sections 1-5; image always fills the vacated side.
- display_dominance: 124px / 16px = 7.75 (inside 6.0-20.8).
- largest_card_row <= 2: no horizontal rows of 3+ boxed siblings; lists and tables stack vertically.
- imagery_ratio >= 0.3: generated SVG manuscript illustrations as `<img>` at large size in every section.
- elements_per_1k >= 55: content is tables, lists, annotated rows with mono labels — detail, not slogans.
- max_radius 20-40: image panels are 28px-radius opaque frames; controls stay at 6px (never pill).
- hero_asymmetry: hero text sits in the left 45%.

**Added constraint.** Every claim carries a specific (number, unit, or example sentence).
