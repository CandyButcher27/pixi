# DESIGN CONTRACT — university research lab

Direction: medium-density, typography-dominant, present imagery, sharp geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is sparse and deliberate. Few elements, each given room, with restraint doing the work that decoration would.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `together.ai` — centered hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 11.69
- **contrast** `live:iad-lab.ch` — unknown hero, alternating rhythm, none card use, sharp geometry, present imagery, display dominance 21.61
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:iad-lab.ch)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:iad-lab.ch)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:live:iad-lab.ch+outlier:live:www.peppasauce.love)
- `display_dominance <= 30.3` — display scale stays inside the reference range (from median of triple)
- `imagery_ratio >= 0.06` — imagery is present in the references (from contrast:live:iad-lab.ch+outlier:live:www.peppasauce.love)
- `imagery_ratio < 0.3` — imagery is present in the references (from contrast:live:iad-lab.ch+outlier:live:www.peppasauce.love)
- `elements_per_1k >= 28` — density is medium in the references (from near:together.ai)
- `elements_per_1k < 55` — density is medium in the references (from near:together.ai)
- `max_radius <= 5` — geometry is sharp in the references (from contrast:live:iad-lab.ch)

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

## Brief-specific decisions (added — these only add to the inherited constraints)

**Subject.** The Okafor Lab — active matter and soft fluids, Department of Physics, Northfield University (fictional). The page reads like the first spread of a lab notebook: questions, an instrument, papers, people, openings.

**Type.** Display: Fraunces (300 weight, tight tracking, ~128px hero at 17px body = dominance ~7.5). Body: Source Serif 4, 17px. Labels, figure numbers, years, venues: IBM Plex Mono 12-13px uppercase. No sans-serif at all. Font stacks never name Inter, Roboto, Arial, Helvetica or system-ui, even as fallbacks.

**Palette.** Paper `#f2efe7`, ink `#15140f`, rule `#cbc5b6`, muted ink `#6b675c`, one accent vermilion `#c43d1a` used only for figure marks and the active link. One full-bleed ink band inverts it. Flat colour only, no gradients, no shadows, no blur.

**Geometry.** border-radius 0 everywhere. Hierarchy comes from size, weight and the 1px rule, never from boxes.

**Imagery.** Every image is a generated scientific figure drawn to `<canvas>` with a seeded RNG (flow-field streamlines, particle tracks, a kymograph, a floor plan). Each is captioned "Fig. n" in mono, the way a paper would. Target imagery_ratio ~0.12-0.2.

**Section order and anchor side** (text centroid alternates; the side text leaves is always occupied by a figure):
1. Hero — LEFT: lab name as display type + one-paragraph thesis; RIGHT: Fig. 1 streamlines canvas.
2. Questions — RIGHT: four numbered open questions as ruled rows; LEFT: Fig. 2 particle-track canvas.
3. Instrument band (full-bleed, ink) — LEFT: the 4D tracking rig, three measured specs as a ruled list; RIGHT: Fig. 3 kymograph canvas.
4. Papers — RIGHT: selected papers as a ruled table (year / title + authors / venue); LEFT: short sticky heading and a link to the full list.
5. People — LEFT: ruled roster (name, role, working on); RIGHT: Fig. 4 floor plan of room 214.
6. Join — RIGHT: open positions and how to write to us; LEFT: short display word and a small figure.
Footer stays under 180px so it does not count as a section.

**Cards.** No card grids. Ruled rows only; borders sit on row containers, never on equal-width sibling cells.
