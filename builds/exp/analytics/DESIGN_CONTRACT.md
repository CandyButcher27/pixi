# DESIGN CONTRACT — developer analytics platform for backend engineers

Direction: medium-density, typography-dominant, absent imagery, pill geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are posthog-nemotron-ultra for fit, vercel for contrast, terminal for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `posthog-nemotron-ultra` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 3.0
- **contrast** `vercel` — centered hero, alternating rhythm, none card use, pill geometry, absent imagery, display dominance 3.0
- **outlier** `terminal` — left hero, uniform rhythm, none card use, rounded geometry, absent imagery, display dominance 1.0

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:vercel)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:vercel)
- `display_dominance >= 2.5` — display typography carries the hierarchy instead of card chrome (from near:posthog-nemotron-ultra)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:vercel+outlier:terminal)
- `max_radius <= 20` — geometry stays inside the reference range (from near:posthog-nemotron-ultra+outlier:terminal)

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

---

## Brief-specific decisions

**Product**: "Tally" — a request-tracing / query-analytics platform for backend
engineers. The concept is a literal ledger: every request is a line item,
every endpoint has a running tally of p50/p99/error-rate, and the whole page
reads as a ledger of running text and ruled rows rather than a catalogue of
feature cards. This is the structural answer to "information as a sequence,
not a row of equal boxes" in the design intent.

### Typefaces (added constraint — none of these are a generic default)

- **Display** — `Gambarino` (self-hosted; the same woff2 already vendored at
  `portfolio-concepts/agenticos/assets/fonts/Gambarino-Regular.woff2`,
  base64-embedded via `@font-face` so the page stays a single file with zero
  network requests). Used only for H1/H2 and the footer wordmark. Fallback
  chain `Georgia, 'Iowan Old Style', serif` never becomes the rendered face
  because the font is embedded, but it keeps the declared stack honest.
- **Body** — `Charter` (`'Iowan Old Style', Georgia, serif` fallback). A
  considered print-quality serif for running prose — deliberately not a
  grotesk sans, so the page doesn't fall into the Inter/Geist "SaaS voice"
  either of the reference set uses.
- **Mono** — `ui-monospace, 'Cascadia Mono', Consolas, 'SF Mono', monospace`,
  reserved *only* for data: the trace waterfall, the endpoint ledger table,
  and uppercase eyebrow labels. Never used for body prose — the slop law's
  "monospace as the house voice" tell is the terminal reference's own
  gimmick, not something to import wholesale here.

### Palette (added constraint)

Dark ink canvas with one cream "paper" insert band, and a single accent —
no gradients, no purple/blue default, no amber (already the terminal
reference's signature):

| token | value | use |
|---|---|---|
| `--bg` | `#0B0E12` | page canvas |
| `--bg-raised` | `#12161C` | chart / table panels |
| `--ink` | `#ECE7DD` | primary text on dark |
| `--ink-dim` | `#8D9199` | secondary text on dark |
| `--hairline` | `#262B33` | rules/dividers on dark |
| `--accent` | `#4FD1C5` | links, live indicator, chart primary series, CTA fill |
| `--accent-ink` | `#06211F` | text set on top of accent fill |
| `--danger` | `#F2755B` | error-rate figures only — never decorative |
| `--paper` | `#EDE6D6` | the one full-bleed inverted band |
| `--paper-ink` | `#1B1712` | text on the paper band |

### Section order (top to bottom)

1. `header` (nav — excluded from measurement by design, kept plain: wordmark,
   4 links, one small solid CTA)
2. **Hero** — prose column left (eyebrow, H1, subhead, one solid CTA + one
   plain text link, an inline running-text proof line), a real SVG trace
   waterfall (labeled spans across 6 real service names, axis ticks in ms)
   right. Text mass sits left → satisfies `hero_asymmetry`.
3. **Full-bleed stack strip** — the one section that inverts to the paper
   palette and spans the full viewport width edge-to-edge, breaking the
   content container → satisfies `full_bleed_sections`. Centered text
   (real technology names: PostgreSQL, Kafka, gRPC, Redis, ClickHouse,
   OpenTelemetry, Envoy, Kubernetes — not invented client logos).
4. **Trace section** — mirrors the hero: a small real SVG service-dependency
   diagram left, prose + a 4-item ruled list (not cards) right → this is the
   first alternation.
5. **Ledger section** — prose left, a real compact endpoint table (mono
   figures, ruled rows, no cell backgrounds) right → second alternation,
   giving `centroid_flips >= 2` across sections 4/5/6.
6. **Alerting section** — small text badges (Slack / PagerDuty / Opsgenie /
   Webhook) left, prose + a 3-item ruled list right → third alternation.
7. **Closing statement** — one serif line, one solid CTA, one mono caveat
   line. No gradient CTA banner, no pricing tiers, no testimonial card.
8. `footer` — Gambarino wordmark (sized below the hero H1), four plain link
   columns (no boxes), colophon line.

### Composition mandates realised structurally

- `full_bleed_sections >= 1` → the cream paper strip (§3), width 100vw,
  height > 200px, opaque background, genuinely inverted register — not just
  a technically-full-width transparent wrapper.
- `centroid_flips >= 2` → the hero (left) → trace section (right) → ledger
  section (left) → alerting section (right) alternation gives three
  transitions between non-centered sections, twice the requirement.
- `display_dominance >= 2.5` → hero H1 renders ~76px against a 17px body
  baseline (ratio ≈ 4.5).
- `largest_card_row <= 2` → no feature grid anywhere. Every list of 3+
  items (capabilities, alert behaviors, footer links) is a stacked,
  hairline-ruled sequence with no per-item background/border/radius, so it
  never registers as an equal-width boxed row.
- `max_radius <= 20` → every radius in the system (buttons, panels, the
  table) sits at 0–8px; nothing approaches pill geometry.

### Prohibitions realised structurally

- `gradients <= 0` → every fill in CSS and in the inline SVGs is a flat
  color; no linear/radial gradient anywhere on the page.
- `pill_controls <= 0` → both buttons use an 4-6px radius, far under
  their own height / 2.
- `glass_panels <= 0` → no `backdrop-filter` anywhere.
- `generic_display_font == False` → the largest text on the page (hero H1)
  is set in the embedded `Gambarino` face.
- `hero_asymmetry >= 0.08` → the hero's text column is the left ~58% of the
  row; the waterfall panel on the right carries almost no text, so the
  weighted centroid sits well left of center.

### Explicitly avoided (slop law)

No fake macOS/traffic-light window, no fake syntax-highlighted code
snippet, no three-tier pricing block, no testimonial quote card, no
gradient pre-footer CTA banner, no floating tag pinned to an image, no
graph-paper background, no gradient-circle avatars, no invented client
logos.
