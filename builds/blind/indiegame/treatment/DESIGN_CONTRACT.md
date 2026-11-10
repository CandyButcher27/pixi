# DESIGN CONTRACT — indie video game launch

Direction: high-density, typography-dominant, dominant imagery, soft geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.
- Read as one system, the references are playstation for fit, live:milkshake.app for contrast, live:labs.chaingpt.org for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `playstation` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 3.38
- **contrast** `live:milkshake.app` — left hero, uniform rhythm, high card use, pill geometry, dominant imagery, display dominance 6.0
- **outlier** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:milkshake.app)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:labs.chaingpt.org)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:labs.chaingpt.org)
- `display_dominance <= 8.4` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:playstation+contrast:live:milkshake.app)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from contrast:live:milkshake.app+outlier:live:labs.chaingpt.org)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:milkshake.app+outlier:live:labs.chaingpt.org)
- `max_radius >= 6` — geometry is soft in the references (from outlier:live:labs.chaingpt.org)
- `max_radius <= 19` — geometry is soft in the references (from outlier:live:labs.chaingpt.org)

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

## Brief-specific decisions (mine)

**Product.** *SALTMARROW*, a pixel-art sailing roguelite by a two-person studio (Low Tide Works, Bergen). Launches 14 March 2027 on Steam, Switch, PS5. $18.99. The page sells it with specifics: run lengths, seed counts, fish species, frame budget, patch cadence, system requirements.

**Typefaces.**
- Display: `Big Shoulders Display` 800, condensed, set at 112px in the hero (body 16px -> dominance 7.0; inside 6.0–8.4). Section heads 64–80px.
- Body: `Atkinson Hyperlegible` 16px.
- Data/labels: `Silkscreen` (pixel face) for stat labels, HUD captions, and table heads — ties type to the game's own UI.

**Palette (flat, no gradients).** Abyss `#0e1719` page, bone `#efe6d2` text and the full-bleed band, flare `#ff5b2e` accent/CTA, kelp `#5d8a63`, brine `#2a4a4e` secondary surface.

**Section order and how each mandate lands.**
1. Nav — wordmark, links, wishlist button (radius 8px, ~44px tall: not a pill).
2. Hero — text block left (title, pitch, launch facts, CTAs) / large pixel canvas right (live sea scene). Text centroid well left of 0.42.
3. "The sea" — canvas LEFT, dense text + stat column RIGHT. Flip 1.
4. "Systems" — text + numbered mechanics list LEFT, tall canvas of the boat cross-section RIGHT. Flip 2.
5. Full-bleed bone band (width 100vw, opaque) — launch roadmap/patch cadence: text right, bestiary canvas strip left. Flip 3. This is the `full_bleed_sections` section.
6. Specs + press — left-weighted requirements table and press figures with a canvas map on the right. Flip 4.
7. Footer — dense fine print.

**Added constraints.**
- Every half a section's text leaves is filled by a canvas of equal or greater height — never empty margin.
- Imagery is procedural `<canvas>` pixel art (no external images), scaled with `image-rendering: pixelated`; together >= 30% of page area.
- Radius: controls and panels 8–14px; nothing >= 20px, nothing fully rounded.
- No card grids of 3+ equal boxed tiles; information is carried by type scale, rules and pixel labels.
- No backdrop-filter, no gradients anywhere (including canvas-free CSS).
