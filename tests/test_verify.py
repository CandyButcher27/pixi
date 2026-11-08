"""The verifier's own falsification test.

A page can dodge every AI tell and still be Generic Corporate Landing Page #47.
GENERIC below satisfies all five prohibitions on purpose. If it passes verification,
the verifier is a checklist measuring compliance with its own assumptions, and the
composition mandates are doing nothing.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from designmcp import contract as contract_mod, verify as verify_mod  # noqa: E402

REFS = {
    "near": {"id": "ref-near", "grammar": {
        "hero_alignment": "left", "section_rhythm": "uniform", "card_reliance": "low",
        "geometry": "soft", "imagery": "present", "density": "low", "text_density": "medium",
        "display_dominance": 8.0, "max_radius": 8, "full_bleed_sections": 0, "sections": 5}},
    "contrast": {"id": "ref-contrast", "grammar": {
        "hero_alignment": "left", "section_rhythm": "alternating", "card_reliance": "none",
        "geometry": "sharp", "imagery": "absent", "density": "high", "text_density": "high",
        "display_dominance": 9.0, "max_radius": 0, "full_bleed_sections": 2, "sections": 6}},
    "outlier": {"id": "ref-outlier", "grammar": {
        "hero_alignment": "right", "section_rhythm": "alternating", "card_reliance": "none",
        "geometry": "sharp", "imagery": "absent", "density": "low", "text_density": "low",
        "display_dominance": 7.0, "max_radius": 0, "full_bleed_sections": 1, "sections": 4}},
}

GENERIC = """<!doctype html><html><head><meta charset="utf-8"><style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font: 16px Georgia, serif; color: #1a1a1a; background: #fff; }
.wrap { max-width: 1100px; margin: 0 auto; padding: 0 24px; }
nav { padding: 20px 0; }
section { padding: 72px 0; }
h1 { font-size: 32px; }
h2 { font-size: 24px; margin-bottom: 16px; }
p { margin-top: 12px; max-width: 640px; }
.btn { display: inline-block; margin-top: 24px; padding: 12px 24px; border-radius: 8px;
       background: #1a1a1a; color: #fff; text-decoration: none; }
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.card { border: 1px solid #e2e2e2; border-radius: 8px; padding: 24px; }
</style></head><body><div class="wrap">
<nav>Acme &nbsp; Product &nbsp; Pricing &nbsp; Docs</nav>
<section><h1>Ship your product faster</h1>
<p>Everything your team needs to plan, build and launch, in one place. Trusted by
thousands of teams who care about moving quickly without breaking what already works.</p>
<a class="btn" href="#">Get started</a></section>
<section><h2>Why teams choose us</h2><div class="cards">
<div class="card"><h3>Fast</h3><p>Set up in minutes, not weeks, with sensible defaults.</p></div>
<div class="card"><h3>Secure</h3><p>Encryption in transit and at rest, audited every year.</p></div>
<div class="card"><h3>Scalable</h3><p>From your first user to your millionth without a rewrite.</p></div>
</div></section>
<section><h2>Loved by teams</h2><p>"It changed how we work." — a customer</p></section>
<section><h2>Start today</h2><p>Free for 14 days. No card required.</p>
<a class="btn" href="#">Get started</a></section>
</div></body></html>"""

DISTINCTIVE = """<!doctype html><html><head><meta charset="utf-8"><style>
* { margin: 0; padding: 0; box-sizing: border-box; border-radius: 0; }
body { font: 16px "Chronicle Text", Georgia, serif; color: #12100c; background: #f4f0e8; }
nav { padding: 20px 40px; }
section { padding: 96px 40px; }
.left { width: 46%; }
.right { width: 46%; margin-left: 54%; }
h1 { font-size: 132px; line-height: 0.92; font-weight: 800; letter-spacing: -0.04em; }
h2 { font-size: 72px; line-height: 1; font-weight: 800; }
p { margin-top: 20px; font-size: 18px; }
.bleed { width: 100vw; margin-left: 0; background: #12100c; color: #f4f0e8; padding: 120px 40px; }
.rule { border-top: 1px solid #12100c; }
.btn { display: inline-block; margin-top: 32px; padding: 16px 28px; border: 1px solid currentColor;
       text-decoration: none; color: inherit; }
</style></head><body>
<nav>ATLAS &nbsp;&nbsp; INDEX &nbsp;&nbsp; ARCHIVE</nav>
<section><div class="left"><h1>Field notes from the edge of the grid</h1>
<p>A publication about infrastructure, written for the people who maintain it rather
than the people who buy it.</p><a class="btn" href="#">Read the current issue</a></div></section>
<section class="bleed"><div class="right"><h2>Issue 04 — Cold storage</h2>
<p>What happens to a dataset nobody has read in eleven years, and who pays to keep
it readable. Reported over four months across three continents.</p></div></section>
<section class="rule"><div class="left"><h2>The archive</h2>
<p>Every issue since 2019, in full, with the working notes and the raw interviews
attached to each piece. Nothing behind a wall.</p></div></section>
<section class="bleed"><div class="right"><h2>Subscribe</h2>
<p>Twelve issues a year, posted. No newsletter, no app, no tracking pixel.</p>
<a class="btn" href="#">Take a subscription</a></div></section>
</body></html>"""


def _write(tmp_path: Path, name: str, html: str) -> Path:
    p = tmp_path / name
    p.write_text(html, encoding="utf-8")
    return p


def test_generic_page_passes_prohibitions_but_fails_the_mandates(tmp_path):
    c = contract_mod.build(REFS)
    result = verify_mod.verify(_write(tmp_path, "generic.html", GENERIC), c)

    assert all(p["passed"] for p in result["prohibitions"]), \
        f"fixture is meant to dodge every tell: {[p for p in result['prohibitions'] if not p['passed']]}"
    assert not result["passed"], "a generic page passed verification — the mandates are doing nothing"
    failed = {m["rule"] for m in result["mandates"] if not m["passed"]}
    assert "largest_card_row" in failed and "display_dominance" in failed, failed


def test_distinctive_page_passes(tmp_path):
    c = contract_mod.build(REFS)
    result = verify_mod.verify(_write(tmp_path, "distinctive.html", DISTINCTIVE), c)
    assert result["passed"], verify_mod.report(result)


def test_contract_carries_positive_mandates_not_only_prohibitions():
    c = contract_mod.build(REFS)
    rules = {r["rule"] for r in c["inherited"]["required"]}
    assert {"full_bleed_sections", "centroid_flips", "display_dominance"} <= rules, rules


def test_bands_follow_the_triple_in_both_directions():
    def refs(**overrides):
        return {role: {"id": f"ref-{role}", "grammar": {**r["grammar"], **overrides}}
                for role, r in REFS.items()}

    def rules(c):
        return {(r["rule"], r["op"], r["value"]) for r in c["inherited"]["required"]}

    image_right = rules(contract_mod.build(refs(hero_alignment="right", imagery="dominant",
                                                geometry="rounded", density="high")))
    bare_left = rules(contract_mod.build(refs(hero_alignment="left", imagery="absent",
                                              geometry="sharp", density="low")))

    assert {("hero_weight_split", ">=", 0.58), ("imagery_ratio", ">=", 0.30),
            ("max_radius", ">=", 20), ("elements_per_1k", ">=", 55)} <= image_right
    assert {("hero_weight_split", "<=", 0.42), ("imagery_ratio", "<", 0.06),
            ("max_radius", "<=", 5), ("elements_per_1k", "<", 28)} <= bare_left


def test_direction_line_agrees_with_the_bands():
    grammars = {role: dict(r["grammar"]) for role, r in REFS.items()}
    grammars["contrast"]["imagery"] = "dominant"
    grammars["near"]["imagery"] = "absent"
    c =contract_mod.build({role: {"id": f"ref-{role}", "grammar": g} for role, g in grammars.items()})
    imagery_rules = {(r["op"], r["value"]) for r in c["inherited"]["required"] if r["rule"] == "imagery_ratio"}
    assert imagery_rules == {("<", 0.06)}
    assert "absent imagery" in c["identity"]["direction"]
