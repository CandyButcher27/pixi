# Blind pairwise test — 25 briefs, tool vs no tool

One human rater (the project owner), 2026-11-10. Each pair: same brief, one page built from the
plain request (control), one built through the design-build protocol with two-way mandates
(treatment). Sides randomised, arm hidden until the rating was posted (`scripts/blind.py`).

## Headline

| outcome | count |
|---|---|
| treatment preferred | 14 |
| control preferred | 9 |
| tie | 2 |
| both generic | 0 |

Treatment won 14 of 23 decisive pairs (61%). Two-sided sign test p = 0.40; 95% CI 41%–78%.
Without the wedding pair (the only build with real photographs): 13 of 22, p = 0.52.

**Not a significant win.** At a true 61% preference, about 100 pairs would be needed to reach
p < 0.05.

## The pattern inside it (post hoc — a hypothesis, not a result)

Split by what the treatment contract said about imagery:

| contract imagery rule | treatment | control | tie |
|---|---|---|---|
| imagery required (`imagery_ratio >= 0.3`, or 0.06–0.3) | 10 | 0 | 2 |
| imagery forbidden (`imagery_ratio < 0.06`) | 4 | 9 | 0 |

Every control page measured near-zero imagery. So:

- Where the tool forced substantial illustration, it never lost.
- Where the tool forbade illustration and both pages were type-only, the plain prompt won 9 of 13.

The imagery-forbidden band comes from the reference majority, and the 85-entry catalogue is
83/85 imageless brand homages. The rule is inheriting a corpus artefact, not a design choice.

## Confounds

- Images and effort move together: treatment builds that needed imagery drew large canvas/SVG
  art, which is more work and more visual content. "Add illustration" alone might explain the
  whole effect.
- Imagery-required contracts came from different reference triples (live award sites) than
  imagery-forbidden ones (catalogue entries), so reference source is mixed in too.
- Control agents inherited this project's anti-generic instructions and skill descriptions,
  so control is stronger than a truly plain prompt.
- One rater. `measure.py` may undercount small inline SVG in control pages.

## What would settle the open question

A third arm: the plain request plus one line, "include substantial original illustration".
If it matches treatment on the 12 imagery pairs, the tool's measured value is "use images",
and the mandate machinery adds nothing on top.
