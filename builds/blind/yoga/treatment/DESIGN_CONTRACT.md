# DESIGN CONTRACT — yoga studio

Direction: medium-density, typography-dominant, dominant imagery, soft geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are live:wanderful.index.studio for fit, mistral.ai for contrast, live:betteroff.studio for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:wanderful.index.studio` — right hero, uniform rhythm, low card use, pill geometry, dominant imagery, display dominance 9.23
- **contrast** `mistral.ai` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 5.25
- **outlier** `live:betteroff.studio` — unknown hero, uniform rhythm, low card use, soft geometry, dominant imagery, display dominance 23.75

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:mistral.ai)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:betteroff.studio)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:wanderful.index.studio+outlier:live:betteroff.studio)
- `display_dominance <= 12.9` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split >= 0.58` — hero_alignment is right in the references (from near:live:wanderful.index.studio)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from near:live:wanderful.index.studio+outlier:live:betteroff.studio)
- `elements_per_1k >= 28` — density is medium in the references (from near:live:wanderful.index.studio+contrast:mistral.ai)
- `elements_per_1k < 55` — density is medium in the references (from near:live:wanderful.index.studio+contrast:mistral.ai)
- `max_radius >= 6` — geometry is soft in the references (from outlier:live:betteroff.studio)
- `max_radius <= 19` — geometry is soft in the references (from outlier:live:betteroff.studio)

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

- **Studio**: "Slow Hours", a yoga studio in a converted letterpress print shop. Message: practice at the speed of the room; classes listed like a printed timetable.
- **Type**: display `Gloock` (high-contrast serif), body `Hanken Grotesk` 17px. Hero h1 ~132px (display_dominance ~7.8, inside 6.0–12.9). Hierarchy by size and weight only; no shadows, no borders on text blocks.
- **Palette** (flat, no gradients): oat `#efe6d8` ground, ink `#1f1a14`, clay `#b4532a`, ochre `#d9a441`, sage `#7d8a6a`, plum night `#2e2226` for the full-bleed band.
- **Section order**: nav -> hero (illustration left, type right) -> this week's timetable as ruled table rows -> full-bleed dusk band (imagery edge to edge) -> four practices as a numbered ruled list beside one tall image -> teachers as ruled rows with small portraits -> passes as a ruled price list -> visit/first-class offer + footer.
- **Mandate realisation**:
  - `hero_weight_split >= 0.58` / `hero_asymmetry`: hero text column occupies the right 52%; the left is a tall illustration (not empty margin).
  - `full_bleed_sections >= 1`: the dusk band is a 100vw section with a plum background and an edge-to-edge illustration.
  - `largest_card_row <= 2`: no boxed sibling rows; timetable, practices, teachers and passes are rows in a vertical sequence.
  - `imagery_ratio >= 0.3`: hero art, dusk band, practices image, teacher portraits and visit image are inline SVG data-URI artworks (self-contained, no network).
  - `max_radius` 6–19: images and the offer panel use 14px radius; buttons use 6px (never pill).
  - `elements_per_1k` 28–55: rows carry several small cells (time, class, teacher, level) to keep medium density.
- **Added constraint**: no row of three-or-more equal boxes anywhere, even unboxed ones under 120px wide are avoided where they would read as cards.
