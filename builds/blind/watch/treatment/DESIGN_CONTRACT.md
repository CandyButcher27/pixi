# DESIGN CONTRACT — luxury watch brand

Direction: low-density, typography-dominant, absent imagery, sharp geometry, uniform section rhythm

## Design intent

- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are bugatti for fit, ferrari for contrast, live:heavn-one.webflow.io for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `bugatti` — right hero, uniform rhythm, high card use, pill geometry, absent imagery, display dominance 4.0
- **contrast** `ferrari` — left hero, uniform rhythm, high card use, sharp geometry, absent imagery, display dominance 5.0
- **outlier** `live:heavn-one.webflow.io` — right hero, alternating rhythm, none card use, rounded geometry, dominant imagery, display dominance 8.57

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:ferrari)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from outlier:live:heavn-one.webflow.io)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:heavn-one.webflow.io)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `hero_weight_split >= 0.58` — hero_alignment is right in the references (from near:bugatti+outlier:live:heavn-one.webflow.io)
- `imagery_ratio < 0.06` — imagery is absent in the references (from near:bugatti+contrast:ferrari)
- `elements_per_1k < 28` — density is low in the references (from near:bugatti+outlier:live:heavn-one.webflow.io)
- `max_radius <= 5` — geometry is sharp in the references (from contrast:ferrari)

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

## Brief-specific decisions (mine — additive only)

- Brand: Vauclair, a fictional independent Vallée de Joux maker. Message: time made slowly, by few hands, in small numbers.
- Display face: Bodoni Moda (high-contrast didone, 400/500). Body: IBM Plex Sans Condensed 300/400. Specs and the live clock: IBM Plex Mono. No Inter/system-ui anywhere.
- Palette: bone #ECE6DA (page), ink #15140F (text), brass #8C6B2E (single accent, hairlines and numerals only), deep loden #1C2621 (the full-bleed band). Flat fills only, no gradients.
- Section order and anchor side (centroid_flips realised as R, L, R, L, R):
  1. Hero — headline and lede on the right two-thirds; the left third carries a mono specification column and the live time in the house's own numerals, so the left side has content, not margin.
  2. Atelier — full-bleed loden band breaking the container; statement on the left, the fourteen-month sequence as a numbered list on the right.
  3. Collection — three references as typographic rows (name in display, specs in mono, price), right-weighted; no cards, no boxes. A left rail holds the edition counts.
  4. Provenance — a long-form quote on the left; the right holds the service guarantees in small type.
  5. Appointment — right-weighted invitation with a single square CTA; left holds the salon addresses.
- Display scale: h1 112px on a 16px body (dominance 7.0, inside 6.0–8.0). No other text above 112px.
- Geometry: every radius 0. CTA is a hairline-bordered rectangle. Hierarchy from size, weight and letter-spacing; dividers are 1px brass hairlines, no shadows.
- Imagery: none. No img, video, canvas or background images. The watch is described, not pictured.
- Density: lean markup, target under 20 elements per 1000px.
- Right-anchored sections (hero, appointment) set their anchor column flush right, so the type itself, not just the column, sits on the right. Provenance uses a 3:1 split so the quote owns the left.

