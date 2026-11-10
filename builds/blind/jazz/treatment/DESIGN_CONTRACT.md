# DESIGN CONTRACT — jazz record label

Direction: medium-density, typography-dominant, dominant imagery, sharp geometry, alternating section rhythm

## Design intent

- Information is expressed as sequences and spatial hierarchy — lists, tables, ruled rows, running text — not as a catalogue of equal cards.
- The visual anchor moves through the page rather than sitting in one column, and the side it leaves should carry weight of its own, not empty margin.
- Typography carries the hierarchy. Size, weight and spacing do the work that borders, shadows and container chrome would otherwise do.
- Read as one system, the references are starchart for fit, vercel for contrast, live:www.peppasauce.love for the unusual grammar. Build in the space they bound — not a copy of any one of them.

The mandates below prevent known failure modes. The intent above is what they are for — satisfying the numbers while violating the intent is a failed build.

## References

- **near** `starchart` — unknown hero, uniform rhythm, high card use, sharp geometry, dominant imagery, display dominance 3.81
- **contrast** `vercel` — centered hero, alternating rhythm, none card use, pill geometry, absent imagery, display dominance 3.0
- **outlier** `live:www.peppasauce.love` — unknown hero, alternating rhythm, none card use, rounded geometry, present imagery, display dominance 41.14

## Composition mandates (inherited — may not be weakened)

- `full_bleed_sections >= 1` — at least one section breaks the page container (from contrast:vercel)
- `centroid_flips >= 2` — visual anchor alternates sides between major sections (from contrast:vercel)
- `display_dominance >= 6.0` — display typography carries the hierarchy instead of card chrome (from outlier:live:www.peppasauce.love)
- `largest_card_row <= 2` — information is a sequence, not a row of equal boxes (from contrast:vercel+outlier:live:www.peppasauce.love)
- `display_dominance <= 8.0` — display scale stays inside the reference range (from median of triple)
- `imagery_ratio >= 0.3` — imagery is dominant in the references (from near:starchart)
- `elements_per_1k >= 28` — density is medium in the references (from near:starchart+contrast:vercel)
- `elements_per_1k < 55` — density is medium in the references (from near:starchart+contrast:vercel)
- `max_radius <= 5` — geometry is sharp in the references (from near:starchart)

## Prohibitions (inherited — may not be weakened)

- `gradients <= 0` — gradient backdrops are the loudest AI tell (from slop_law)
- `pill_controls <= 0` — fully rounded pill CTAs (from slop_law)
- `glass_panels <= 0` — glassmorphism panels (from slop_law)
- `generic_display_font == False` — Inter / system-ui defaults on the display face (from slop_law)
- `hero_asymmetry >= 0.08` — centred hero column is the default AI composition (from slop_law)

## Brief-specific decisions (added — none weaken the above)

**Label:** Late Set Records, a fictional small jazz label. Every record is cut live, one room, two-track tape, no overdubs. The page reads like a catalogue sheet plus a sleeve back.

**Typefaces**
- Display: Bodoni Moda (high-contrast didone, the old liner-note headline face). Fallback stack is just `serif`, with no generic sans anywhere in the display stack.
- Body: Newsreader (text serif, reads like liner notes).
- Data: IBM Plex Mono for catalogue numbers, matrix codes, durations and dates. It plays the role of the stamped label on a sleeve.

**Palette** (flat fills only, no gradients)
- Paper `#ece3cf`, ink `#15120e`, oxblood `#8e2a1c`, brass `#d6a02a`, smoke teal `#1f4746`, plus a dark band `#15120e` with paper text.

**Scale**
- Body is 16px. The single largest display line is 112px (ratio 7.0, inside 6.0–8.0). Section heads run 56–72px. Hierarchy comes from size and weight, never from boxes.

**Section order, with the anchor side for each** (text left = L, text right = R)
1. Hero (L): the label name and its manifesto on the left. The right half is one large generative sleeve (canvas), so the empty side carries the image, not margin.
2. New release (R): the large sleeve sits on the left. On the right are the title and a tracklist as ruled rows (number, title, composer, duration).
3. Catalogue (L): a full-bleed ink band. A ruled table of releases (cat. no., artist, title, year, format) sits on the left, with a tall sleeve column on the right.
4. Roster (R): a portrait-format sleeve on the left. On the right, the musicians are a ruled list with instrument and session count.
5. Live sets (L): dates as ruled rows on the left, a club-poster sleeve on the right.
6. Subscription (R): the art on the left. On the right, the "Standing order" copy and a sharp-cornered form.

**Structural rules added**
- All imagery is generative record-sleeve art drawn on `<canvas>`: flat colour blocks, discs, bars and stamped type, in the style of mid-century sleeves. It has to cover at least 30% of the page area through big asymmetric pieces, not a grid.
- No row of three or more equal boxed siblings. Listings are table and list rows divided by 1px rules, never cards.
- Border radius is 0 everywhere. Buttons are rectangles in ink or oxblood.
- No marquee, no testimonial strip, no three-up feature cards, no centred hero.
- Below 820px every section stacks with the art first and the text after, which keeps the rules hairlines.
