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

## Standouts (second pass, 2026-11-10)

All 50 screenshots shown unlabelled in random order (`/gallery` in `scripts/blind.py`); the
rater starred the ones that stood out. Picks in `standouts.json`.

| version | starred |
|---|---|
| treatment | 4: cyber, dental, jazz, writer |
| control | 3: codeschool, jazz, ramen |

- Every starred treatment page is one whose contract required imagery (ratio 0.30–0.39).
  None of the 13 imagery-forbidden treatment pages was starred.
- Two of the three starred control pages (codeschool, ramen) are pairs control won.
- The rater named jazz as the favourite and starred both jazz pages; in the pairwise round the
  treatment jazz page ("Late Set Records", canvas-drawn sleeves) won.
- Standouts split 4–3: no sign that the tool produces exceptional pages more often. They
  agree with the imagery pattern above.

Measurement caveat this exposed: the control jazz page has a grid of eight CSS-drawn album
covers yet measures `imagery_ratio` 0.00, because `measure.py` counts img/canvas/svg/video area,
not CSS-drawn shapes. "Control pages have no imagery" partly reflects what the probe can see.

## Third arm: plain request + one illustration line (2026-11-10)

On the 10 briefs where the treatment contract required imagery (wedding and lab left out), a
third version was built from the plain request plus: "Include substantial original
illustration as a primary part of the page: draw it yourself in SVG or canvas." Rated blind
against treatment by the same rater (`ratings_treatment_illustrated.jsonl`).

| | treatment | illustration prompt | tie |
|---|---|---|---|
| vs plain prompt (round 1, these 10 briefs) | 8 | 0 | 2 |
| vs illustration prompt (this round) | 6 | 4 | 0 |

Treatment won archstudio, cyber, dental, hotel, indiegame, jazz; the one-line version won
bakery, ceramics, writer, yoga. 6–4 is two-sided p = 0.75: indistinguishable from even.

**Reading:** on these briefs one sentence of prompt closes most of the gap the tool opened
against the plain prompt (8–0 becomes 6–4). Whatever the tool adds beyond "draw
illustrations" is too small to detect at 10 pairs. The tool costs more per page (≈85k tokens
and ≈15 actions vs ≈70k and 2–5).

Found while building: `measure.py` does not count inline `<svg>` as imagery, so 9 of the 10
illustrated pages measure `imagery_ratio` 0.00. Imagery numbers in contracts and in the
catalogue understate SVG art.

## Fourth arm: illustration prompt + a screenshot reference (2026-11-10)

Five briefs rebuilt from the illustration prompt plus one screenshot of a live award-gallery
site chosen to sit outside the recurring style (references in `references.json`; screenshots
stay local). Rated blind against the illustration-prompt pages
(`ratings_illustrated_referenced.jsonl`). House-style score = count of seven recurring traits
(`blind.py style`).

| brief | reference | house style: prompt → +reference | preferred |
|---|---|---|---|
| bakery | ju.st | 5 → 2 | reference |
| jazz | superlocaldesign.com | 4 → 2 | reference |
| writer | thursday.studio | 6 → 3 | reference |
| cyber | oxide.computer | 6 → 4 | reference |
| yoga | howmanyplants.com | 4 → 4 | prompt only |

Reference arm preferred 4–1 (two-sided p = 0.38; five pairs is too few for significance).
Mean house-style score 5.0 → 3.0. The one loss is the one pair whose score did not move: its
reference already used a paper background and mono labels.

Two references were rejected before building because their screenshots showed an age gate
or PHP warnings; picking references needs a visual check.
