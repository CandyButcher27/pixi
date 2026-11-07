# First protocol run — five briefs

Run of `search_designs -> get_design_contract -> DESIGN_CONTRACT.md -> build -> verify_build`.
Selection and contracts logged in `run-log.md` before anything was built, so the causal chain
is inspectable. Per-build artefacts: `<slug>/DESIGN_CONTRACT.md`, `contract.json`,
`index.html`, `screenshot.png`.

Result: 5/5 pass contract compliance. One needed a repair round.

| brief | near | contrast | outlier | result |
|---|---|---|---|---|
| developer analytics platform | posthog-nemotron-ultra | vercel | terminal | 10/10 first pass |
| independent coffee roaster | agenticos | terminal | tesla | 10/10 first pass |
| legal case management | physics | tesla | terminal | 9/9 first pass |
| experimental music festival | runwayml | terminal | supabase | 9/9 first pass |
| hardware robotics startup | nintendo | meta | terminal | 8/9, repaired to 9/9 |

## The question that matters: is the chain traceable?

For each build, a visible design decision traced back to a specific retrieved grammar:

- **roaster** — the 168px `Slow Roast` wordmark exists because `display_dominance >= 6.0` was
  inherited from `near:agenticos`, which measures 13.75x. Nothing else in the brief asked for
  a masthead that size.
- **roaster** — the oxblood full-width bands come from `full_bleed_sections >= 1`, inherited
  from `outlier:tesla` (11 full-bleed sections).
- **roaster / caselaw / analytics** — none of them has a three-card feature row, because
  `largest_card_row <= 2` was inherited from card-free references. The information became a
  definition list, a numbered ruled index, and a data table respectively.
- **festival** — the left/right alternating room blocks come from `centroid_flips >= 2`,
  inherited from `outlier:supabase`, the only alternating-rhythm entry in that triple.
- **robotics** — the 84px uppercase headline comes from `display_dominance >= 3.2`, inherited
  from `contrast:meta` (4.0x).

So the answer is yes: every distinctive property of these pages maps to a named reference and
a named rule. The retrieval and contract layers are not ornamental.

## Failure modes observed

1. **The alternation mandate is satisfied by empty space.** `centroid_flips >= 2` only requires
   the centre of mass to swap sides. Four of the five builds satisfy it by shifting a column
   right and leaving the other half of the section empty. The composition alternates; it is not
   necessarily *composed*. This is the same shape of problem as prohibitions-only contracts, one
   level up — a mandate that constrains an axis without constraining what happens on the axis.
   Candidate next dimension: something that reads the balance of the empty side.
2. **The generic-font check is substring-based and over-fires.** `Roboto Condensed` and
   `Arial Narrow` are distinct typefaces, but they contain `roboto` and `arial`, so the robotics
   build failed on a display face that was not actually a default. The repair was to change the
   stack rather than weaken the rule — correct under the protocol, but the rule should
   eventually match a face, not a substring. (Counterpoint for keeping it strict: on a machine
   without those faces installed, the stack really does fall back to a generic.)
3. **The far pool is small.** `terminal` took contrast-or-outlier in 4 of 5 briefs, `tesla` in 2.
   With 72/85 entries card-heavy and 77/85 uniform-rhythm, there are only a handful of entries
   the separation gate can reach. The mechanism works; the corpus is the bottleneck, exactly as
   predicted.
4. **A measurement bug was caught by inspecting the triples, not the pages.** `tesla` reported
   `hero_weight_split 2.483` — a ratio that must lie in 0..1 — because off-viewport text in an
   overflow track dragged the centre of mass past the page edge, and `hero_alignment: right` was
   derived from that. Fixed by clamping each text rect's centre to the viewport before weighting.
   Had the triples not been logged first, this would have surfaced as an unexplainable page.

## What this run does not show

The agent that built these pages is the same one that built the system, in the same session,
with the contract visible in context. That is the weakest possible version of the test. The
claim it supports is "the contract is buildable against and the verifier catches violations" —
not "an uninstructed agent is measurably forced out of its default grammar". That needs a
fresh session with only the MCP connected, and ideally a control arm with no MCP at all.
