# DESIGN CONTRACT — architecture studio in Copenhagen

Direction: low-density, typography-dominant, dominant imagery, soft geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is sparse and deliberate. Few elements, each given room, with restraint doing the work that decoration would.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:designed.space` — left hero, uniform rhythm, low card use, pill geometry, dominant imagery, display dominance 1.0
- **contrast** `live:www.pelizzari.com` — centered hero, uniform rhythm, none card use, pill geometry, present imagery, display dominance 13.36
- **outlier** `live:www.hyperframe.com` — unknown hero, alternating rhythm, none card use, soft geometry, dominant imagery, display dominance 16.25

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:www.pelizzari.com)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.hyperframe.com)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.hyperframe.com)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:designed.space+contrast:live:www.pelizzari.com+outlier:live:www.hyperframe.com)
- `display_dominance <= 18.7` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:live:designed.space)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from near:live:designed.space+outlier:live:www.hyperframe.com)
- `elements_per_1k < 28` — density is low in the references (from near:live:designed.space+contrast:live:www.pelizzari.com)
- `max_radius >= 6` — geometry is soft in the references (from outlier:live:www.hyperframe.com)
- `max_radius <= 19` — geometry is soft in the references (from outlier:live:www.hyperframe.com)

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

- **Studio**: Ravn & Søgaard Tegnestue, Christianshavn. Housing, schools, harbour structures in brick, timber, lime.
- **Typefaces**: display Instrument Serif (400, 148px hero = 9.25x body); body Archivo 16px. No Inter/system fallback on display.
- **Palette**: paper #ece6da, drawing ground #e2dacb, ink #1d2320, Copenhagen brick #a2472c (accent only), harbour #34504f (full-bleed band). Flat fills only, no gradients.
- **Imagery**: architectural line drawings rendered to `<canvas>` (elevation, plan, section, harbour bath, site plan) — the studio's own medium, not stock photos. Imagery share must stay >= 0.30.
- **Section order and anchor side** (each vacated side holds a drawing, never empty margin):
  1. Hero — text left (cols 1-5), facade elevation right (cols 6-12).
  2. Practice — plan drawing left, statement right.
  3. Selected work — ruled list of four projects left; sticky drawing right that redraws on hover/focus of a row.
  4. Full-bleed harbour band — harbour bath elevation edge to edge, quote top-right.
  5. Method — numbered ruled sequence left, section drawing right.
  6. Contact — site plan left, address + single CTA right.
- **Hierarchy**: done with type size and hairline rules (1px rgba ink), no cards, shadows or boxed containers. Project list and method are sequences, never a card row.
- **Geometry**: drawing panels radius 12px, CTA radius 8px (never pill). Full-bleed band radius 0.
- **Density**: one CTA total, < 28 elements per 1000px.
