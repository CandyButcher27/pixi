# DESIGN CONTRACT — podcast network

Direction: medium-density, balanced-hierarchy, absent imagery, sharp geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is sparse and deliberate. Few elements, each given room, with restraint doing the work that decoration would.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `mastercard` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 8.0
- **contrast** `live:workmode.show` — unknown hero, uniform rhythm, none card use, sharp geometry, absent imagery, display dominance 2.0
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from outlier:live:www.peppasauce.love)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:www.peppasauce.love)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:live:workmode.show+outlier:live:www.peppasauce.love)
- `display_dominance <= 11.2` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:mastercard)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:mastercard+contrast:live:workmode.show)
- `elements_per_1k >= 28` — density is medium in the references (from near:mastercard)
- `elements_per_1k < 55` — density is medium in the references (from near:mastercard)
- `max_radius <= 5` — geometry is sharp in the references (from contrast:live:workmode.show)

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

## Brief-specific decisions (added — Undertow Audio, an independent podcast network)

### Message
Undertow is a small network of nine slow, reported shows. The page reads like a broadcast
schedule / programme log: who is on, what aired this week, how the shows get made, how to pitch or advertise.

### Typefaces
- Display: **Big Shoulders Display** 800 (condensed, broadcast-signage). Never Inter/system-ui.
- Body / running text: **Newsreader** (text serif) at 16px.
- Data (timestamps, durations, episode numbers): **IBM Plex Mono** 400/500.

### Palette (flat, no gradients)
- Paper `#EEEAE1`, ink `#16140F`, muted ink `#6B665B`, rule `#C9C3B5`
- Signal `#D9441C` (on-air red, used for live markers and the single CTA only)
- Night band `#16140F` with paper text for the full-bleed roster section

### Section order and anchor side (centroid alternation)
1. Hero — LEFT. 128px wordmark headline + dek in the left 60%; right 40% carries the "on air now" log
   (a real list, not empty margin) but lighter than the headline so the centroid stays <= 0.42.
2. Roster (full-bleed night band) — RIGHT. Heading, dek and the 9-show ruled table fill the right two thirds;
   the narrow left column carries a 112px signal-red "09" count so the left side holds weight, not margin.
3. This week — LEFT. Episode log as ruled rows (no., title, show, duration, play) in the left two thirds; right third holds a short editor's note.
4. Method — RIGHT. Small section number left; manifesto running text and a numbered ruled list on the right.
5. Pitch / advertise — LEFT. Two text columns max (never 3), unboxed, with one sharp signal-red CTA.
6. Footer.

### Structural rules I add
- Every section is a direct child of `<main>` so the measured centroids are the designed ones.
- Only one size reaches display scale: the hero headline at 128px on a 16px body (dominance 8.0).
  Section headings top out at 64px.
- No boxed items side by side: lists are stacked ruled rows (border-top only), never card grids.
- All radii 0; buttons are rectangles with a 1px ink border.
- No images; the waveform motif is CSS bars (`span` elements), so imagery stays absent.
- Restraint: one accent colour, used only for "live" and the primary CTA.
