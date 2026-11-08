# Control vs treatment — fresh sessions, three briefs

Six fresh agents, same model, three briefs, two arms.

- **Control** — the ordinary request only ("Build a landing page for X, single self-contained
  index.html"). Built outside the repo, in a scratchpad directory, so this project's
  `CLAUDE.md` could not reach it.
- **Treatment** — same brief plus the design-build protocol: freeze a contract, read the
  intent and mandates, write the brief-specific half, build, verify, repair.

Deviation from a clean design, recorded honestly: subagents inherit this repo's `CLAUDE.md`,
which now instructs agents to use the protocol. Control agents therefore received one extra
line telling them not to use the catalogue, the skill, or the MCP. That removes the machinery
without hinting at what a good page looks like — but it is not a pure ordinary request.

Treatment results were re-verified in the parent session rather than trusted from the agents'
own reports. All three pass: analytics 10/10, roaster 10/10, festival 9/9. Two passed on the
first build with no repair round.

## Measured grammar

| page | hero | rhythm | full-bleed | cards | largest row | geometry | radius | display | density |
|---|---|---|---|---|---|---|---|---|---|
| analytics/control | left | alternating | 0 | high | 4 | soft | 12 | 2.88 | high |
| analytics/treatment | left | alternating | 3 | none | 0 | soft | 6 | 4.47 | high |
| roaster/control | right | uniform | 2 | low | 2 | sharp | 0 | 5.0 | medium |
| roaster/treatment | left | alternating | 4 | none | 0 | soft | 12 | 7.19 | medium |
| festival/control | centered | uniform | 0 | none | 0 | sharp | 0 | 11.0 | medium |
| festival/treatment | left | alternating | 2 | none | 0 | soft | 16 | 9.5 | low |

## Result 1 — the treatment eliminates the generic tells

Slop tells present, counted independently of any contract (0 of 8 is best):

| page | tells |
|---|---|
| analytics/control | **4** — glass panels, generic display font, 4-up card row, no full-bleed |
| analytics/treatment | **0** |
| roaster/control | **2** — gradient backdrop, uniform rhythm |
| roaster/treatment | **0** |
| festival/control | **4** — centred hero, generic display font, uniform rhythm, no full-bleed |
| festival/treatment | **0** |

The screenshots agree with the numbers. Control/analytics is the archetype: pill badge over a
centred-ish hero, a six-card feature grid, a stat strip, three pricing tiers with the middle one
highlighted "MOST USED", a centred closing CTA. Treatment/analytics has a serif display face, a
cream full-bleed band interrupting the dark page, numbered hairline-ruled sequences where the
cards would be, and no pricing trio at all.

Cross-arm grammar distance per brief: analytics 0.302, roaster 0.537, festival 0.529. The arms
land in different compositional regions.

## Result 2 — but the treatment converges across briefs

Mean pairwise grammar distance *within* an arm — how different the three briefs' pages are from
each other:

    control     0.565
    treatment   0.221

**The treatment arm is less varied across briefs than the control arm.** Every treatment page is
left hero, alternating rhythm, card-free, soft geometry, high display dominance. A coffee
roaster, a developer analytics tool and an experimental music festival came out structurally
similar.

This is mode collapse again, one level up: the system removed the model's default attractor and
substituted its own. Not the intended outcome, and the honest reading of it is that the win in
Result 1 is a win against *slop*, not yet a win for *differentiation*.

Two causes, both visible in the data:

1. **The mandate vocabulary is narrow.** Five rule types (`full_bleed_sections`,
   `centroid_flips`, `display_dominance`, `largest_card_row`, `max_radius`) fire in nearly the
   same configuration every time, so every contract says roughly the same thing.
2. **The far pool is tiny.** `terminal` appeared in all three triples, `supabase` in two. With
   72/85 corpus entries card-heavy and 77/85 uniform-rhythm, the separation gate can only reach
   a handful of entries, so the contrast and outlier references barely change between briefs.

Caveat on the comparison: the control arm's higher variance is partly variance *in how each page
is generic* — one centred with a gradient, one card-heavy, one uniform. Spread among failure
modes is not a virtue. But the metric is measuring compositional region, and the treatment's
region really is narrower.

## What this changes

The next work is not another verifier rule. It is the two causes above:

- Derive mandates from what makes a given triple *distinctive* rather than emitting the same
  five rule types every time, so two different triples produce two different contracts.
- Widen corpus grammar coverage so the contrast and outlier slots are not drawn from the same
  three entries — the dataset task, now with a measurement attached to it.

## Rerun after adding live gallery sites (2026-11-08, `builds/exp2/`)

Same three briefs, three fresh treatment agents, same protocol. The only change is the
reference pool: 461 measured live award-gallery sites joined the 85 catalogue entries, and the
outlier is now picked by brief relevance among the rarest fifth. Control was not rebuilt
(its pages are gone); its recorded 0.565 stands.

| brief | near | contrast | outlier | verify |
|---|---|---|---|---|
| analytics | posthog-nemotron-ultra | vercel | live:peppasauce.love | 10/10 |
| roaster | agenticos | live:coffeesupreme.com | live:peppasauce.love | 10/10 |
| festival | live:midlife.engineering | live:easound.no | live:superlocaldesign.com | 9/9 |

    within-arm mean pairwise distance
    control (recorded)   0.565
    treatment, exp       0.221   (remeasured with the current probe: unchanged)
    treatment, exp2      0.276

Pairs: analytics–roaster 0.200 -> 0.258, analytics–festival 0.241 -> 0.396,
roaster–festival 0.222 -> 0.173.

**Convergence eased slightly but did not go away.** All three exp2 pages are left hero,
card-free, sharp geometry (radius 2–3px), medium density. Last run they were all soft; now
they are all sharp. Imagery and rhythm moved (two pages now carry imagery; festival is
uniform), which accounts for most of the gain.

Reading: a wider reference pool changes what the triples say, but the contract still emits the
same five mandate types (`full_bleed_sections`, `centroid_flips`, `display_dominance`,
`largest_card_row`, `max_radius`) with almost the same values. The agents fill every dimension
the contract leaves free with the same house style: ruled tables in place of cards, a 2px
radius, a left-anchored oversized headline. The corpus bottleneck is relieved; the mandate
vocabulary is now the binding constraint.

## Rerun with two-way mandates (2026-11-08, `builds/exp3/`)

Contracts now carry bands on hero side, imagery, density and geometry, set by the reference
majority and able to point either way, plus a ceiling on display size. Before any build, over
30 briefs: distinct mandate sets 12 -> 25, mean Jaccard distance between contracts
0.318 -> 0.576.

| brief | hero | geometry | imagery | density | verify |
|---|---|---|---|---|---|
| analytics | left | rounded (28px) | absent | high | 15/15 |
| roaster | left | sharp (0px) | absent | high | 14/14 |
| festival | right | rounded (28px) | absent | high | 14/14 |

    within-arm mean pairwise distance
    control (recorded)   0.565
    exp  (fixed mandates)        0.221
    exp2 (+ live reference pool) 0.276
    exp3 (+ two-way mandates)    0.392

Pairs: analytics–roaster 0.349, analytics–festival 0.282, roaster–festival 0.544.

**The contract is the lever.** The pages moved apart on exactly the axes where their contracts
differed: hero side (festival's contract demanded a right-weighted hero) and geometry. Where
all three contracts agreed (no imagery, high density, card-light), all three pages agree too.
The remaining gap to control comes from those three briefs' triples agreeing with each other,
not from the agent ignoring the contract.

Two new gaming patterns:
- `max_radius >= 20` is met by a single 28px panel on a page that is otherwise square
  (analytics, festival). `max_radius` reads the largest radius only, so "rounded geometry" can
  be one element.
- The direction line was taken from the contrast reference alone and could contradict a band
  (roaster: direction said dominant imagery, band said < 0.06). Fixed: direction now uses
  the same majority.
