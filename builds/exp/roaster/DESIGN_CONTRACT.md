# DESIGN CONTRACT — independent coffee roaster in Lisbon

Direction: low-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is sparse and deliberate. Few elements, each given room, with restraint doing the work that decoration would.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

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

## Brief-specific decisions — independent coffee roaster in Lisbon

Brand: **Torra** — a micro-roastery on Rua de São Paulo, Cais do Sodré, Lisboa.

### Typefaces
- Display (headlines, numerals, pull-quotes): `"Iowan Old Style", "Sitka Text", Georgia, serif` — a warm literary serif, self-falls-back through the system, never Inter/system-ui/-apple-system/Segoe UI/Roboto/Helvetica Neue/Arial.
- Body (running text, addresses, tasting notes): `Charter, Georgia, serif`.
- Label/data (eyebrows, roast temps, coordinates, hours): `ui-monospace, "Cascadia Code", Menlo, Consolas, monospace`.
- No font files or Google Fonts links are loaded — the page must stay a single self-contained file with no external assets, so the distinctiveness comes from an unusual *stack*, not a webfont.

### Palette
Warm kraft-paper canvas + espresso ink + a single azulejo-teal accent, with one full-bleed dark-espresso band. No hue overlaps with the amber/oxblood palettes already used elsewhere in this repo's portfolio set.
- `--canvas: #F4EBDD` (kraft paper)
- `--canvas-line: #DCCEB4` (hairline rule on canvas)
- `--ink: #241C15` (espresso, warm near-black)
- `--ink-dim: #6B5D4D`
- `--accent: #1F6B63` (azulejo teal — the one chromatic event on the page)
- `--accent-deep: #153F3A`
- `--dark-bg: #1B1410` (dark-roast band, full-bleed section only)
- `--dark-ink: #F4EBDD`
- `--dark-dim: #9C8E7E`

### Section order
1. `header` — nav (excluded from measured "sections" by tag; solid canvas background, no blur)
2. `hero` — headline + subhead + CTA (left) / roast-curve diagram (right)
3. `process` — "how we roast" pull-quote (left) / four-step ruled sequence (right)
4. `origins` — sourcing table of three origin lots (left) / compass + coordinates (right)
5. `visit` — full-bleed dark-espresso band — azulejo line-art motif (left) / address & hours (right)
6. `footer` — wordmark, colophon, unboxed link columns

### How each composition mandate is realised structurally
- `full_bleed_sections >= 1` → the `visit` section alone spans edge-to-edge with an opaque dark-espresso background; every other section sits on the plain canvas so the full-bleed band reads as a deliberate event, not a repeated pattern.
- `centroid_flips >= 2` → text mass alternates left → right → left → right across hero → process → origins → visit (three flips, one full flip of margin over the two required).
- `display_dominance >= 6.0` → the hero H1 is set with `clamp(56px, 8vw, 124px)` against a 16px body — the single largest type on the page, well past the 6× floor.
- `largest_card_row <= 2` → the origin lots and the roast steps are ruled, stacked sequences (table rows / vertical list items), never a side-by-side equal-width grid; nav and footer link columns carry no background, border, or radius so they can never register as a "card row" even where they sit side by side.
- `max_radius <= 20` → every panel and control radius is 10px (12px on the hero diagram frame), well inside the ceiling.

### How each prohibition is honored
- `gradients <= 0` → no `gradient(...)` anywhere; texture comes from hairline rules, borders, and the SVG line-art motif, never a gradient fill.
- `pill_controls <= 0` → the one CTA (`.cta`) is ~52px tall with a 10px radius (pill threshold would be ~25px) — nowhere close.
- `glass_panels <= 0` → no `backdrop-filter`; the nav is a flat, opaque canvas panel.
- `generic_display_font == False` → every element sized off the display stack above; the largest-type element on the page is always styled with `--font-display`.
- `hero_asymmetry >= 0.08` → the hero is a 1.4fr/1fr grid with the dense headline+subhead+CTA column on the left and a text-light diagram on the right, pushing the measured centroid to roughly 0.30–0.35 (asymmetry ≈ 0.15–0.20).
