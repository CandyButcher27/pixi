"""Measure control and treatment builds side by side.

The verifier score answers "did this build satisfy its contract". This answers the
question the experiment is actually about: did the two arms land in different
compositional regions, and does either look like the default AI landing page.

Usage:
  .venv/Scripts/python.exe scripts/compare_arms.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from designmcp import catalogue, measure, verify as verify_mod  # noqa: E402

CONTROL = Path(r"C:\Users\sriva\AppData\Local\Temp\claude\C--Users-sriva-Desktop-frontend"
               r"\c1729627-4ab5-4c11-8c92-2a5444a4a649\scratchpad\control")
TREATMENT = ROOT / "builds" / (sys.argv[1] if len(sys.argv) > 1 else "exp")
SLUGS = ["analytics", "roaster", "festival"]

FIELDS = ["hero_alignment", "section_rhythm", "full_bleed_sections", "card_reliance",
          "largest_card_row", "geometry", "max_radius", "display_dominance", "density"]


def main():
    pages, labels = [], []
    for slug in SLUGS:
        for arm, root in (("control", CONTROL), ("treatment", TREATMENT)):
            p = root / slug / "index.html"
            if p.exists():
                pages.append(p)
                labels.append(f"{slug}/{arm}")
            else:
                print(f"missing: {p}")

    # measured one at a time: measure_many keys by parent directory name, which collides
    # across arms (control/analytics and treatment/analytics are both "analytics")
    grammars = {label: measure.grammar(measure.measure(page)) for label, page in zip(labels, pages)}

    print(f"{'':34}" + "".join(f"{f[:15]:>17}" for f in FIELDS))
    for label in labels:
        g = grammars[label]
        print(f"{label:34}" + "".join(f"{str(g.get(f)):>17}" for f in FIELDS))

    print("\nslop tells present (lower is better):")
    for label in labels:
        s = verify_mod.slop_score(grammars[label])
        print(f"  {label:24} {s['score']}/{s['of']}  {', '.join(s['tells']) or '-'}")

    print("\ngrammar distance between arms, per brief:")
    for slug in SLUGS:
        a, b = f"{slug}/control", f"{slug}/treatment"
        if a in grammars and b in grammars:
            d = catalogue.distance({"grammar": grammars[a]}, {"grammar": grammars[b]})
            print(f"  {slug:12} {d:.3f}")

    print("\nwithin-arm convergence (how alike are the three briefs in one arm):")
    for arm in ("control", "treatment"):
        ds = []
        for i, s1 in enumerate(SLUGS):
            for s2 in SLUGS[i + 1:]:
                a, b = f"{s1}/{arm}", f"{s2}/{arm}"
                if a in grammars and b in grammars:
                    ds.append(catalogue.distance({"grammar": grammars[a]}, {"grammar": grammars[b]}))
        if ds:
            print(f"  {arm:12} mean pairwise distance {sum(ds) / len(ds):.3f}  (low = every brief got the same page)")


if __name__ == "__main__":
    main()
