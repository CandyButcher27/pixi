# DESIGN CONTRACT — sustainable fashion label

Direction: medium-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is sparse and deliberate. Few elements, each given room, with restraint doing the work that decoration would.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `vercel` — centered hero, alternating rhythm, none card use, pill geometry, absent imagery, display dominance 3.0
- **contrast** `terminal` — left hero, uniform rhythm, none card use, rounded geometry, absent imagery, display dominance 1.0
- **outlier** `live:uk.organicbasics.com` — centered hero, alternating rhythm, low card use, pill geometry, dominant imagery, display dominance 11.79

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from outlier:live:uk.organicbasics.com)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:uk.organicbasics.com)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:uk.organicbasics.com)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:vercel+contrast:terminal+outlier:live:uk.organicbasics.com)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split <= 0.42` — hero_alignment is left in the references (from contrast:terminal)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:vercel+contrast:terminal)
- `elements_per_1k >= 28` — density is medium in the references (from near:vercel)
- `elements_per_1k < 55` — density is medium in the references (from near:vercel)
- `max_radius >= 20` — geometry is rounded in the references (from contrast:terminal)
- `max_radius <= 40` — geometry is rounded in the references (from contrast:terminal)

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

## Brief-specific decisions (added — inherited constraints above are unchanged)

**Label:** Fallow — a clothing label that makes one small season a year and lets the land (and the wardrobe) rest between. The page sells restraint: fewer pieces, full cost transparency, lifetime repair.

**Typefaces:** display `Gloock` (high-contrast serif, editorial, not a default); body `Work Sans` 16px. No Inter / system-ui anywhere.

**Palette:** undyed linen `#ECE5D6` page, ink `#1E1C17` text, madder red `#9E3B24` single accent (links, one CTA, numerals), indigo-dark `#1F2A33` full-bleed ledger band with linen text. No gradients, no glass.

**Section order and how each mandate is realised:**
1. Hero — LEFT. Headline "Fewer clothes, worn longer." at the display size, plus a short paragraph and CTA, left two-thirds. The right third holds a ruled four-row fact list (season, pieces, fibres, virgin synthetics) so the right side carries weight without pulling the text centroid past 0.42.
2. Season 07 — RIGHT. Left column: a sticky 96px "Season 07" heading alone. Right column: intro paragraph, then a ruled list (not cards) of the season's pieces with fibre, mill and price. The long list pulls the anchor right; the display heading keeps the left side weighted.
3. The ledger — LEFT, FULL-BLEED. Dark indigo band spanning the viewport. Left: running text and a ruled cost breakdown of one jacket. Right: the jacket's total set large in display type inside a 24px-radius panel.
4. Repair, for life — RIGHT. Left: short display heading "Bring it back." Right: running text plus a numbered 3-step sequence.
5. Footer / letter — LEFT. Sign-up form for the once-a-year season letter, address and small print.

**Numbers:** display at clamp(56px, 7.8vw, 112px) → 112px at 1440 = 7.0x body (inside 6.0–8.0). Radius 20px on all controls (height 54px, so never a pill), 24px on panels — rounded geometry is a system, not one panel. No images, no equal-box rows: all lists are ruled rows with bottom borders only.

**Added constraints:** one accent colour only; no testimonials, no logo strip, no marquee, no icon-grid.
