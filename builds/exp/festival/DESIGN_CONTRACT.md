# DESIGN CONTRACT — experimental electronic music festival

Direction: low-density, balanced-hierarchy, absent imagery, rounded geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is sparse and deliberate. Few elements, each given room, with restraint doing the work that decoration would.
- Read as one system, the references are runwayml for fit, terminal for contrast, supabase for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `runwayml` — left hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 4.5
- **contrast** `terminal` — left hero, uniform rhythm, none card use, rounded geometry, absent imagery, display dominance 1.0
- **outlier** `supabase` — centered hero, alternating rhythm, high card use, soft geometry, absent imagery, display dominance 4.0

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from outlier:supabase)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:supabase)
- `display_dominance >= 3.6` — display typography carries the hierarchy instead of card chrome (from near:runwayml)
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

---

## Brief-specific decisions (agent-owned, appended after freeze)

Festival identity: **AUXFIELD IX** — "an experimental electronic music festival," three days,
one disused industrial signal-relay yard, two rooms, no headliners — the curatorial premise is
that hierarchy itself (headliner vs. support) is the thing being rejected, which is also why the
page rejects the templated hero+3-cards hierarchy.

### Typefaces (neither is a generic default)

- **Display**: `"Bahnschrift", "Cascadia Code", monospace`, driven to a heavy condensed cut via
  `font-variation-settings: "wght" 700, "wdth" 62.5` (Bahnschrift is a variable font — this is
  not the default weight/width anyone gets by naming the family). Condensed industrial grotesk
  reads as technical signage, which is the actual visual language of touring rave/warehouse
  flyers, not a SaaS marketing face.
- **Body / data**: `"Consolas", "Cascadia Mono", monospace` — every schedule row, price, and
  meta line is set in monospace so the lineup reads as a manifest/readout, not prose. One
  technical system end to end; no third face is introduced anywhere.
- Neither stack contains `inter`, `system-ui`, `-apple-system`, `segoe ui`, `roboto`,
  `helvetica neue`, or `arial` in any fallback position (checked against the full declared
  stack, not just the first name).

### Palette (within "absent imagery, rounded geometry")

| token | hex | use |
|---|---|---|
| `--void` | `#0B0B0C` | primary ground |
| `--void-2` | `#151517` | raised panel on void |
| `--paper` | `#F3F0E7` | the one inverted full-bleed section |
| `--ink` | `#F5F3EE` | text on void |
| `--ink-dim` | `#8B8A85` | secondary text on void |
| `--ink-on-paper` | `#0B0B0C` | text on paper |
| `--ink-on-paper-dim` | `#57554C` | secondary text on paper |
| `--acid` | `#D6FF3E` | single primary accent — CTA, index numerals, active state |
| `--signal` | `#FF3B63` | single secondary accent — scarcity/status tags only, never decorative |
| `--line` | `#2B2B2D` | hairline rule on void |
| `--line-paper` | `#D8D2BE` | hairline rule on paper |

No gradient is used anywhere (not even `repeating-linear-gradient` for texture) — solid fields,
rules, and type do all the work. No imagery, per the inherited direction: the page is entirely
typographic/graphic.

### Section order and why

1. `nav` (fixed, excluded from composition measurement by tag) — wordmark + live-transmission tag.
2. `section.hero` — massive condensed headline, left-set (~30% weighted centroid). Realises
   `hero_asymmetry` and starts the alternation.
3. `section.manifesto` — **full-bleed** (`100vw`, explicit `--paper` background) inverted light
   panel, a right-set pull-quote. Realises `full_bleed_sections >= 1` and is flip 1
   (left → right).
4. `section.lineup` — the roster as a left-set monospace manifest (index / act / stage / time),
   not a card grid. Flip 2 (right → left).
5. `section.stages` — two-room breakdown; copy is deliberately weighted into a wide right column
   (soundsystem specs) against a short left label, swinging the centroid right again (flip 3).
6. `section.tickets` — access tiers as a left-set vertical ledger (not equal-width cards), back
   to the left (flip 4 — well past the `>= 2` floor, so measurement noise on any one section
   can't fail the mandate).
7. `footer` — centered credits/socials, low text mass, closes the page without overriding the
   rhythm already established.

### How each inherited mandate is realised structurally

- **`full_bleed_sections >= 1`**: `section.manifesto` and `section.stages` both carry an explicit
  opaque `background-color` and are pulled to `100vw` via negative margin — two independent
  full-bleed breaks, not one, so the mandate holds even if one is measured differently than
  intended.
- **`centroid_flips >= 2`**: the hero→manifesto→lineup→stages→tickets sequence alternates
  left/right weighted text mass four times (see section order above), by actually moving where
  the dominant column and copy volume sit, not by re-labelling `text-align`.
- **`display_dominance >= 3.6`**: body/data type is fixed at 16px; the hero headline runs
  `clamp(4.5rem, 11vw, 9.5rem)` (72–152px), giving a ratio of roughly 4.5–9.5, comfortably clear
  of the floor at any viewport.
- **`max_radius <= 20`**: every rounded surface (ticket rows, manifesto card, nav pill-less tag)
  is capped at `16px`; the CTA button uses `8px` — nowhere near `height / 2`, so it also can't
  register as a pill control.
- **`gradients <= 0` / `pill_controls <= 0` / `glass_panels <= 0` / `generic_display_font ==
  False` / `hero_asymmetry >= 0.08`**: no gradient function, no blurred/translucent panel, no
  radius approaching half the control height, and no generic family in the display stack appear
  anywhere in the stylesheet — verified by grep before the first `verify` run, not just by
  intent.
