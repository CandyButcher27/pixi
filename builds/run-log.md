# Protocol run log

## analytics — "developer analytics platform for backend engineers"

NEAR  posthog-nemotron-ultra  (relevance 1.0, novelty 0.386, distance from near 0.0)
  left hero 0.343 | uniform rhythm | 7 full-bleed | high cards (row 4) | pill 6px | display 3.0x | absent imagery | high density
CONTRAST  vercel  (relevance 0.406, novelty 0.51, distance from near 0.492)
  centered hero 0.5 | alternating rhythm | 6 full-bleed | none cards (row 0) | pill 100px | display 3.0x | absent imagery | medium density
OUTLIER  terminal  (relevance 0.0, novelty 0.619, distance from near 0.572)
  left hero 0.326 | uniform rhythm | 0 full-bleed | none cards (row 0) | rounded 20px | display 1.0x | absent imagery | low density

CONTRACT (inherited)
  direction: medium-density, typography-dominant, absent imagery, pill geometry, alternating section rhythm
  required:
    full_bleed_sections >= 1   <- contrast:vercel
    centroid_flips >= 2   <- contrast:vercel
    display_dominance >= 2.5   <- near:posthog-nemotron-ultra
    largest_card_row <= 2   <- contrast:vercel+outlier:terminal
    max_radius <= 20   <- near:posthog-nemotron-ultra+outlier:terminal
  forbidden:
    gradients <= 0   <- slop_law
    pill_controls <= 0   <- slop_law
    glass_panels <= 0   <- slop_law
    generic_display_font == False   <- slop_law
    hero_asymmetry >= 0.08   <- slop_law

VERIFICATION
PASS  contract compliance 10/10
(compliance with the selected design grammar, not a judgement of visual quality)

composition mandates:
  [ok] full_bleed_sections >= 1 — measured 2  <- contrast:vercel
  [ok] centroid_flips >= 2 — measured 3  <- contrast:vercel
  [ok] display_dominance >= 2.5 — measured 5.41  <- near:posthog-nemotron-ultra
  [ok] largest_card_row <= 2 — measured 0  <- contrast:vercel+outlier:terminal
  [ok] max_radius <= 20 — measured 0  <- near:posthog-nemotron-ultra+outlier:terminal
prohibitions:
  [ok] gradients <= 0 — measured 0  <- slop_law
  [ok] pill_controls <= 0 — measured 0  <- slop_law
  [ok] glass_panels <= 0 — measured 0  <- slop_law
  [ok] generic_display_font == False — measured False  <- slop_law
  [ok] hero_asymmetry >= 0.08 — measured 0.3  <- slop_law

## roaster — "independent coffee roaster in Lisbon"

NEAR  agenticos  (relevance 1.0, novelty 0.471, distance from near 0.0)
  left hero 0.298 | uniform rhythm | 7 full-bleed | none cards (row 0) | pill 999px | display 13.75x | absent imagery | medium density
CONTRAST  terminal  (relevance 0.0, novelty 0.619, distance from near 0.548)
  left hero 0.326 | uniform rhythm | 0 full-bleed | none cards (row 0) | rounded 20px | display 1.0x | absent imagery | low density
OUTLIER  supabase  (relevance 0.0, novelty 0.583, distance from near 0.777)
  centered hero 0.468 | alternating rhythm | 8 full-bleed | high cards (row 4) | soft 12px | display 4.0x | absent imagery | high density

CONTRACT (inherited)
  direction: low-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm
  required:
    full_bleed_sections >= 1   <- outlier:supabase
    centroid_flips >= 2   <- outlier:supabase
    display_dominance >= 6.0   <- near:agenticos
    largest_card_row <= 2   <- near:agenticos+contrast:terminal
    max_radius <= 20   <- contrast:terminal+outlier:supabase
  forbidden:
    gradients <= 0   <- slop_law
    pill_controls <= 0   <- slop_law
    glass_panels <= 0   <- slop_law
    generic_display_font == False   <- slop_law
    hero_asymmetry >= 0.08   <- slop_law

VERIFICATION
PASS  contract compliance 10/10
(compliance with the selected design grammar, not a judgement of visual quality)

composition mandates:
  [ok] full_bleed_sections >= 1 — measured 2  <- outlier:supabase
  [ok] centroid_flips >= 2 — measured 3  <- outlier:supabase
  [ok] display_dominance >= 6.0 — measured 10.5  <- near:agenticos
  [ok] largest_card_row <= 2 — measured 0  <- near:agenticos+contrast:terminal
  [ok] max_radius <= 20 — measured 0  <- contrast:terminal+outlier:supabase
prohibitions:
  [ok] gradients <= 0 — measured 0  <- slop_law
  [ok] pill_controls <= 0 — measured 0  <- slop_law
  [ok] glass_panels <= 0 — measured 0  <- slop_law
  [ok] generic_display_font == False — measured False  <- slop_law
  [ok] hero_asymmetry >= 0.08 — measured 0.358  <- slop_law

## caselaw — "legal case management software for small firms"

NEAR  physics  (relevance 1.0, novelty 0.424, distance from near 0.0)
  left hero 0.209 | uniform rhythm | 0 full-bleed | none cards (row 0) | pill 999px | display 4.38x | absent imagery | medium density
CONTRAST  tesla  (relevance 0.489, novelty 0.583, distance from near 0.459)
  right hero 0.9 | uniform rhythm | 11 full-bleed | none cards (row 0) | pill 50px | display 2.84x | absent imagery | high density
OUTLIER  terminal  (relevance 0.0, novelty 0.619, distance from near 0.452)
  left hero 0.326 | uniform rhythm | 0 full-bleed | none cards (row 0) | rounded 20px | display 1.0x | absent imagery | low density

CONTRACT (inherited)
  direction: high-density, balanced-hierarchy, absent imagery, pill geometry, uniform section rhythm
  required:
    full_bleed_sections >= 1   <- contrast:tesla
    display_dominance >= 3.5   <- near:physics
    largest_card_row <= 2   <- near:physics+contrast:tesla+outlier:terminal
    max_radius <= 24   <- contrast:tesla+outlier:terminal
  forbidden:
    gradients <= 0   <- slop_law
    pill_controls <= 0   <- slop_law
    glass_panels <= 0   <- slop_law
    generic_display_font == False   <- slop_law
    hero_asymmetry >= 0.08   <- slop_law

VERIFICATION
PASS  contract compliance 9/9
(compliance with the selected design grammar, not a judgement of visual quality)

composition mandates:
  [ok] full_bleed_sections >= 1 — measured 2  <- contrast:tesla
  [ok] display_dominance >= 3.5 — measured 4.88  <- near:physics
  [ok] largest_card_row <= 2 — measured 0  <- near:physics+contrast:tesla+outlier:terminal
  [ok] max_radius <= 24 — measured 0  <- contrast:tesla+outlier:terminal
prohibitions:
  [ok] gradients <= 0 — measured 0  <- slop_law
  [ok] pill_controls <= 0 — measured 0  <- slop_law
  [ok] glass_panels <= 0 — measured 0  <- slop_law
  [ok] generic_display_font == False — measured False  <- slop_law
  [ok] hero_asymmetry >= 0.08 — measured 0.307  <- slop_law

## festival — "experimental electronic music festival"

NEAR  runwayml  (relevance 1.0, novelty 0.296, distance from near 0.0)
  left hero 0.333 | uniform rhythm | 1 full-bleed | high cards (row 5) | pill 9999px | display 4.5x | absent imagery | medium density
CONTRAST  terminal  (relevance 0.0, novelty 0.619, distance from near 0.582)
  left hero 0.326 | uniform rhythm | 0 full-bleed | none cards (row 0) | rounded 20px | display 1.0x | absent imagery | low density
OUTLIER  supabase  (relevance 0.0, novelty 0.583, distance from near 0.647)
  centered hero 0.468 | alternating rhythm | 8 full-bleed | high cards (row 4) | soft 12px | display 4.0x | absent imagery | high density

CONTRACT (inherited)
  direction: low-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm
  required:
    full_bleed_sections >= 1   <- outlier:supabase
    centroid_flips >= 2   <- outlier:supabase
    display_dominance >= 3.6   <- near:runwayml
    max_radius <= 20   <- contrast:terminal+outlier:supabase
  forbidden:
    gradients <= 0   <- slop_law
    pill_controls <= 0   <- slop_law
    glass_panels <= 0   <- slop_law
    generic_display_font == False   <- slop_law
    hero_asymmetry >= 0.08   <- slop_law

VERIFICATION
PASS  contract compliance 9/9
(compliance with the selected design grammar, not a judgement of visual quality)

composition mandates:
  [ok] full_bleed_sections >= 1 — measured 2  <- outlier:supabase
  [ok] centroid_flips >= 2 — measured 3  <- outlier:supabase
  [ok] display_dominance >= 3.6 — measured 9.5  <- near:runwayml
  [ok] max_radius <= 20 — measured 0  <- contrast:terminal+outlier:supabase
prohibitions:
  [ok] gradients <= 0 — measured 0  <- slop_law
  [ok] pill_controls <= 0 — measured 0  <- slop_law
  [ok] glass_panels <= 0 — measured 0  <- slop_law
  [ok] generic_display_font == False — measured False  <- slop_law
  [ok] hero_asymmetry >= 0.08 — measured 0.363  <- slop_law

## robotics — "hardware robotics startup building warehouse arms"

NEAR  nintendo  (relevance 1.0, novelty 0.582, distance from near 0.0)
  centered hero 0.475 | uniform rhythm | 0 full-bleed | none cards (row 0) | soft 6px | display 3.67x | absent imagery | high density
CONTRAST  meta  (relevance 1.0, novelty 0.408, distance from near 0.681)
  left hero 0.312 | alternating rhythm | 0 full-bleed | high cards (row 4) | pill 999px | display 4.0x | absent imagery | medium density
OUTLIER  terminal  (relevance 0.0, novelty 0.619, distance from near 0.461)
  left hero 0.326 | uniform rhythm | 0 full-bleed | none cards (row 0) | rounded 20px | display 1.0x | absent imagery | low density

CONTRACT (inherited)
  direction: medium-density, typography-dominant, absent imagery, pill geometry, alternating section rhythm
  required:
    centroid_flips >= 2   <- contrast:meta
    display_dominance >= 3.2   <- contrast:meta
    largest_card_row <= 2   <- near:nintendo+outlier:terminal
    max_radius <= 20   <- near:nintendo+outlier:terminal
  forbidden:
    gradients <= 0   <- slop_law
    pill_controls <= 0   <- slop_law
    glass_panels <= 0   <- slop_law
    generic_display_font == False   <- slop_law
    hero_asymmetry >= 0.08   <- slop_law

VERIFICATION
PASS  contract compliance 9/9
(compliance with the selected design grammar, not a judgement of visual quality)

composition mandates:
  [ok] centroid_flips >= 2 — measured 3  <- contrast:meta
  [ok] display_dominance >= 3.2 — measured 5.6  <- contrast:meta
  [ok] largest_card_row <= 2 — measured 0  <- near:nintendo+outlier:terminal
  [ok] max_radius <= 20 — measured 0  <- near:nintendo+outlier:terminal
prohibitions:
  [ok] gradients <= 0 — measured 0  <- slop_law
  [ok] pill_controls <= 0 — measured 0  <- slop_law
  [ok] glass_panels <= 0 — measured 0  <- slop_law
  [ok] generic_display_font == False — measured False  <- slop_law
  [ok] hero_asymmetry >= 0.08 — measured 0.352  <- slop_law
