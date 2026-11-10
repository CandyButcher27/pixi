# DESIGN CONTRACT — portfolio for a ceramic artist

Direction: high-density, typography-dominant, dominant imagery, sharp geometry, alternating section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.
- Read as one system, the references are starbucks for fit, live:ohhmydesign.com for contrast, live:www.twistudio.fr for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `starbucks` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 3.12
- **contrast** `live:ohhmydesign.com` — unknown hero, alternating rhythm, high card use, pill geometry, dominant imagery, display dominance 14.88
- **outlier** `live:www.twistudio.fr` — left hero, alternating rhythm, none card use, pill geometry, dominant imagery, display dominance 2.38

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:ohhmydesign.com)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:ohhmydesign.com)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from contrast:live:ohhmydesign.com)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from near:starbucks+outlier:live:www.twistudio.fr)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from contrast:live:ohhmydesign.com+outlier:live:www.twistudio.fr)
- `elements_per_1k >= 55` — density is high in the references (from contrast:live:ohhmydesign.com+outlier:live:www.twistudio.fr)

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

## Brief-specific decisions (added — these add to, never relax, the above)

- **Subject:** Hilde Aune, wood-fired stoneware and porcelain, Jæren coast studio. The page is a working catalogue, not a mood board: every work carries clay body, cone, firing number, dimensions, status.
- **Typefaces:** display `Gloock` (high-contrast serif, carved feel); text `Hanken Grotesk`; data `JetBrains Mono` for specs, cones, temperatures. No Inter/system-ui anywhere.
- **Scale:** body 16px; the single largest display line is 112px (dominance 7.0, inside the 6–8 band). Nothing else exceeds 96px.
- **Palette:** raw clay paper `#ECE5D8`, ink `#1E1915`, iron-red shino `#9C3D1F`, ash celadon `#7F9180`, kiln black `#15110E`. Flat fills only — no CSS gradients; tonal variation lives inside the imagery.
- **Geometry:** sharp. Border radius 0 on every control and panel; hierarchy from type size, weight, rules and spacing — no cards with shadows.
- **Imagery:** every vessel, tile and kiln view is rendered on `<canvas>` from lathe profiles with procedural glaze, drips, iron speckle and ash; imagery covers ≥ 30% of page area.
- **Section order & anchor side (alternation realised structurally):**
  1. Hero — name, statement, current-kiln facts LEFT; large group-of-vessels canvas RIGHT.
  2. Featured work — moon jar canvas LEFT; long-form text + spec sheet RIGHT.
  3. Kiln (full-bleed, kiln black, canvas spans viewport) — firing log text LEFT; ember/stack image fills the rest.
  4. Works index — tall canvas strip of forms LEFT; dense 20-row catalogue table RIGHT.
  5. Glaze notebook — recipes table LEFT; grid of 12 test-tile canvases RIGHT.
  6. Exhibitions, stockists, commissions — studio image LEFT; dense lists RIGHT.
  7. Footer — contact and studio visits LEFT; empty side carries a wide shard canvas, not margin.
  In every split the non-text side carries an image, never empty margin.
- **Density:** specifics over slogans — numbers, recipes, dates, prices, edition counts.
- **Controls:** text links with an underline rule and one square-cornered "Request a commission" button; no pills.
