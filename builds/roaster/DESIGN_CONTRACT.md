# DESIGN CONTRACT — independent coffee roaster in Lisbon

Direction: low-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm

## References

- **near** `agenticos` — left hero, uniform rhythm, none card use, pill geometry, absent imagery, display dominance 13.75
- **contrast** `terminal` — left hero, uniform rhythm, none card use, rounded geometry, absent imagery, display dominance 1.0
- **outlier** `supabase` — centered hero, alternating rhythm, high card use, soft geometry, absent imagery, display dominance 4.0

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from outlier:supabase)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:supabase)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from near:agenticos)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:agenticos+contrast:terminal)
- `max_radius <= 20` — geometry stays inside the reference range (from contrast:terminal+outlier:supabase)

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
