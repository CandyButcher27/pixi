# DESIGN CONTRACT — cybersecurity consultancy

Direction: high-density, typography-dominant, dominant imagery, rounded geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- The page is dense and rewards reading: specifics, numbers and detail rather than three-word value propositions.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14
- **contrast** `live:labs.chaingpt.org` — unknown hero, alternating rhythm, low card use, soft geometry, dominant imagery, display dominance 12.38
- **outlier** `live:ohhmydesign.com` — unknown hero, alternating rhythm, high card use, pill geometry, dominant imagery, display dominance 14.88

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:live:labs.chaingpt.org)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:live:labs.chaingpt.org)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from near:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from near:live:www.peppasauce.love+contrast:live:labs.chaingpt.org)
- `display_dominance <= 20.8` — display scale stays inside the reference range (from median of triple)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from contrast:live:labs.chaingpt.org+outlier:live:ohhmydesign.com)
- `elements_per_1k >= 55` — density is high in the references (from near:live:www.peppasauce.love+contrast:live:labs.chaingpt.org+outlier:live:ohhmydesign.com)
- `max_radius >= 20` — geometry is rounded in the references (from near:live:www.peppasauce.love)
- `max_radius <= 40` — geometry is rounded in the references (from near:live:www.peppasauce.love)

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

## Brief-specific decisions (added — these add to, never relax, the inherited rules)

- **Studio**: Halvard & Rook — adversarial security consultancy (red team, incident response, OT/ICS, cloud). Voice: field notes, not marketing. Every claim carries a number, a date or a named control.
- **Typefaces**: display `Bricolage Grotesque` (800, tight tracking, opsz 96); reading text `Newsreader` (serif, 16px base so the reading column feels like a report); data `JetBrains Mono` for timestamps, CVE IDs, table figures. Fallback stacks use only `serif` / `monospace` keywords — no generic sans in the display stack.
- **Palette**: bone `#ECE6DA` page, ink `#17140F` text and figure panels, signal orange `#D9481C` (single accent — findings, CTAs, active nodes), moss `#1F3328` for the full-bleed band, muted `#6B6457`. Flat fills only; no gradients, no blur.
- **Scale**: body 16px, h1 132px (ratio 8.25, inside 6.0–20.8). Section heads 56–72px. Nothing else above 80px.
- **Geometry**: figure panels and the form panel radius 28px; buttons 14px radius on a 52px-tall control (well under half-height, so never a pill). Rules (1px ink 18%) separate rows — no card borders, no shadows.
- **Imagery (>= 0.3 of page area)**: every major section carries a large `<canvas>` figure drawn from data — attack-path graph (hero), engagement map (band), service coverage matrix, incident timeline, method phase chart, retainer response histogram. The imagery is the evidence, not decoration.
- **Section order and anchor side** (realises `centroid_flips >= 2` with weight on both sides):
  1. Hero — text left (h1 + dense lede + key facts), attack graph right. Asymmetric, centroid left.
  2. Full-bleed moss band — engagement map left, ruled numbers list right. Centroid right. (`full_bleed_sections >= 1`.)
  3. Services — ruled numbered table of six practices left, coverage matrix figure right. Centroid left.
  4. Case file — incident timeline figure left, T+ timestamped narrative table right. Centroid right.
  5. Method — four-phase ruled sequence left, phase chart right. Centroid left.
  6. Engage — response histogram left, engagement-model table + intake form right. Centroid right.
  7. Footer — dense multi-column index.
- **Cards**: no boxed rows of 3+. Practices, stats, phases and models are table rows or ruled lists (`largest_card_row <= 2`).
- **Density (>= 55 elements per 1000px)**: tables, definition lists and inline mono tags carry specifics; the copy is meant to be read.
