"""Check a built page against its contract by measuring the render.

Positive mandates are checked first and reported first: a page that only avoids the
prohibitions has proved nothing.
"""
from __future__ import annotations

from pathlib import Path

from . import measure

DERIVED = {
    "hero_asymmetry": lambda g, raw: abs(g["hero_weight_split"] - 0.5) if g.get("hero_weight_split") is not None else 0.0,
    "elements_per_1k": lambda g, raw: round(raw["element_count"] / max(raw["page_height"] / 1000, 1), 1),
}

OPS = {
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    "==": lambda a, b: a == b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
}


def metric(grammar: dict, raw: dict, rule: str):
    if rule in DERIVED:
        return DERIVED[rule](grammar, raw)
    if rule in grammar:
        return grammar[rule]
    return raw.get(rule)


def check(grammar: dict, raw: dict, rules: list[dict]) -> list[dict]:
    out = []
    for r in rules:
        value = metric(grammar, raw, r["rule"])
        passed = value is not None and OPS[r["op"]](value, r["value"])
        out.append({"rule": r["rule"], "expected": f"{r['op']} {r['value']}",
                    "measured": value, "passed": bool(passed), "why": r.get("why", ""),
                    "source": r.get("source", "unknown")})
    return out


def verify(page_path: str | Path, contract: dict) -> dict:
    raw = measure.measure(page_path)
    g = measure.grammar(raw)
    if "error" in g:
        return {"passed": False, "error": g["error"]}

    mandates = check(g, raw, contract["inherited"]["required"])
    prohibitions = check(g, raw, contract["inherited"]["forbidden"])
    violations = [c for c in mandates + prohibitions if not c["passed"]]
    return {
        "passed": not violations,
        "mandates": mandates,
        "prohibitions": prohibitions,
        "violations": violations,
        "score": f"{len(mandates + prohibitions) - len(violations)}/{len(mandates + prohibitions)}",
        "score_means": "contract compliance, not visual quality",
        "measured_grammar": g,
    }


def report(result: dict) -> str:
    if "error" in result:
        return f"could not render: {result['error']}"
    lines = [f"{'PASS' if result['passed'] else 'FAIL'}  contract compliance {result['score']}",
             "(compliance with the selected design grammar, not a judgement of visual quality)",
             "", "composition mandates:"]
    for c in result["mandates"]:
        lines.append(f"  [{'ok' if c['passed'] else 'XX'}] {c['rule']} {c['expected']} — "
                     f"measured {c['measured']}  <- {c['source']}")
    lines.append("prohibitions:")
    for c in result["prohibitions"]:
        lines.append(f"  [{'ok' if c['passed'] else 'XX'}] {c['rule']} {c['expected']} — "
                     f"measured {c['measured']}  <- {c['source']}")
    if result["violations"]:
        lines += ["", "fix, in order:"]
        for c in result["violations"]:
            lines.append(f"  - {c['why'] or c['rule']} (needs {c['rule']} {c['expected']}, "
                         f"got {c['measured']}; inherited from {c['source']})")
    return "\n".join(lines)


SLOP_TELLS = [
    ("centred hero", lambda g: g.get("hero_alignment") == "centered"),
    ("gradient backdrop", lambda g: g.get("gradients", 0) > 0),
    ("pill controls", lambda g: g.get("geometry") == "pill"),
    ("glass panels", lambda g: g.get("glass_panels", 0) > 0),
    ("generic display font", lambda g: bool(g.get("generic_display_font"))),
    ("three-or-more equal card row", lambda g: g.get("largest_card_row", 0) >= 3),
    ("uniform section rhythm", lambda g: g.get("section_rhythm") == "uniform"),
    ("no full-bleed section", lambda g: g.get("full_bleed_sections", 0) == 0),
]


def slop_score(grammar: dict) -> dict:
    """Count the default-AI-landing-page tells present in a measured page.

    Independent of any contract: it asks how much the page looks like the thing every
    model produces, not whether it satisfied a particular set of references.
    """
    hits = [name for name, test in SLOP_TELLS if test(grammar)]
    return {"score": len(hits), "of": len(SLOP_TELLS), "tells": hits}
