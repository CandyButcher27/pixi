"""Synthesise the inherited half of a design contract from selected references.

Prohibitions alone produce a page with no tells and no character. Every contract
therefore carries positive composition mandates derived from the contrast and
outlier references — obligations that are hard to satisfy while staying generic.

The agent writes the other half (the brief-specific decisions) and may add
constraints, never weaken these.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from . import catalogue

# Checked against the same measurements used to describe the catalogue.
# op is evaluated as: metric <op> value
SLOP_PROHIBITIONS = [
    {"rule": "gradients", "op": "<=", "value": 0, "source": "slop_law",
     "why": "gradient backdrops are the loudest AI tell"},
    {"rule": "pill_controls", "op": "<=", "value": 0, "source": "slop_law",
     "why": "fully rounded pill CTAs"},
    {"rule": "glass_panels", "op": "<=", "value": 0, "source": "slop_law",
     "why": "glassmorphism panels"},
    {"rule": "generic_display_font", "op": "==", "value": False, "source": "slop_law",
     "why": "Inter / system-ui defaults on the display face"},
    {"rule": "hero_asymmetry", "op": ">=", "value": 0.08, "source": "slop_law",
     "why": "centred hero column is the default AI composition"},
]

MANDATE_FLOOR_DISPLAY = 2.5
MANDATE_CAP_DISPLAY = 6.0   # a reference with 16px body text and a 260px headline is not a mandate
DISPLAY_CEILING_FACTOR = 1.4

# Two-way bands on dimensions the slop law leaves free. Without them every contract
# pushes the same direction and the agent fills the free axes with one house style
# (ISS-8). Thresholds are the bucket edges in measure.grammar. Centred hero is a slop
# tell, so hero bands exist only for a side.
BANDS = [
    ("hero_alignment", "hero_weight_split", {"left": [("<=", 0.42)], "right": [(">=", 0.58)]}),
    ("imagery", "imagery_ratio", {"dominant": [(">=", 0.30)], "present": [(">=", 0.06), ("<", 0.30)],
                                  "absent": [("<", 0.06)]}),
    ("density", "elements_per_1k", {"high": [(">=", 55)], "medium": [(">=", 28), ("<", 55)],
                                    "low": [("<", 28)]}),
    ("geometry", "max_radius", {"sharp": [("<=", 5)], "soft": [(">=", 6), ("<=", 19)],
                                "rounded": [(">=", 20), ("<=", 40)]}),
]
ABSTAIN = {"centered", "unknown", "pill"}  # slop-tell or unmeasured values do not vote


def _majority(grammars: dict[str, dict], field: str) -> tuple[str | None, list[str]]:
    votes: dict[str, list[str]] = {}
    for role, g in grammars.items():
        if g.get(field) not in ABSTAIN:
            votes.setdefault(g.get(field), []).append(role)
    if not votes:
        return None, []
    value, roles = max(votes.items(), key=lambda kv: len(kv[1]))
    if len(roles) >= 2 or "near" not in sum(votes.values(), []):
        return value, roles
    return grammars["near"].get(field), ["near"]


def build(refs: dict[str, dict]) -> dict:
    """refs: {"near": entry, "contrast": entry, "outlier": entry} from catalogue.select."""
    grammars = {role: r["grammar"] for role, r in refs.items()}
    differentiators = [grammars["contrast"], grammars["outlier"]]

    required: list[dict] = []

    if any(g.get("full_bleed_sections", 0) >= 1 for g in differentiators):
        source = next(role for role in ("contrast", "outlier")
                      if grammars[role].get("full_bleed_sections", 0) >= 1)
        required.append({"rule": "full_bleed_sections", "op": ">=", "value": 1,
                         "source": f"{source}:{refs[source]['id']}",
                         "why": "at least one section breaks the page container"})

    if any(g.get("section_rhythm") == "alternating" for g in differentiators):
        source = next(role for role in ("contrast", "outlier")
                      if grammars[role].get("section_rhythm") == "alternating")
        required.append({"rule": "centroid_flips", "op": ">=", "value": 2,
                         "source": f"{source}:{refs[source]['id']}",
                         "why": "visual anchor alternates sides between major sections"})

    loudest = max(grammars, key=lambda role: grammars[role].get("display_dominance", 0))
    display_floor = min(MANDATE_CAP_DISPLAY,
                        max(MANDATE_FLOOR_DISPLAY,
                            round(0.8 * grammars[loudest].get("display_dominance", 0), 1)))
    required.append({"rule": "display_dominance", "op": ">=", "value": display_floor,
                     "source": f"{loudest}:{refs[loudest]['id']}",
                     "why": "display typography carries the hierarchy instead of card chrome"})

    card_light = [role for role, g in grammars.items() if g.get("card_reliance") in ("none", "low")]
    if len(card_light) >= 2:
        required.append({"rule": "largest_card_row", "op": "<=", "value": 2,
                         "source": "+".join(f"{role}:{refs[role]['id']}" for role in card_light),
                         "why": "information is a sequence, not a row of equal boxes"})

    display_target = sorted(g.get("display_dominance", 0) for g in grammars.values())[1]
    required.append({"rule": "display_dominance", "op": "<=",
                     "value": max(display_floor + 2.0, round(DISPLAY_CEILING_FACTOR * display_target, 1)),
                     "source": "median of triple", "why": "display scale stays inside the reference range"})

    for field, metric, bands in BANDS:
        value, roles = _majority(grammars, field)
        source = "+".join(f"{role}:{refs[role]['id']}" for role in roles)
        for op, bound in bands.get(value, []):
            required.append({"rule": metric, "op": op, "value": bound, "source": source,
                             "why": f"{field} is {value} in the references"})

    return {
        "identity": {
            "references": {role: {"id": r["id"], "grammar": r["grammar"]} for role, r in refs.items()},
            "direction": _direction(grammars),
            "design_intent": _intent(grammars, refs),
        },
        "inherited": {"required": required, "forbidden": SLOP_PROHIBITIONS},
        "agent_owns": [
            "product message, section order, and copy",
            "the exact display and body typefaces (must not be a generic default)",
            "the palette, within the direction above",
            "how each composition mandate is realised structurally",
        ],
        "rule": "You may add constraints. You may not weaken or drop an inherited one.",
    }


def _intent(grammars: dict[str, dict], refs: dict[str, dict]) -> list[str]:
    """Why the numbers are what they are.

    The mandates prevent known failure modes; they do not carry the reason behind the
    grammar, and a rule whose reason is missing gets satisfied literally and gamed
    semantically. Two to four sentences, derived from the same measurements.
    """
    out = []
    card_light = [g for g in grammars.values() if g.get("card_reliance") in ("none", "low")]
    if len(card_light) >= 2:
        out.append("Information is expressed as sequences and spatial hierarchy — lists, tables, "
                   "ruled rows, running text — not as a catalogue of equal cards.")
    if any(g.get("section_rhythm") == "alternating" for g in grammars.values()):
        out.append("The visual anchor moves through the page rather than sitting in one column, "
                   "and the side it leaves should carry weight of its own, not empty margin.")
    if max(g.get("display_dominance", 0) for g in grammars.values()) >= 3:
        out.append("Typography carries the hierarchy. Size, weight and spacing do the work that "
                   "borders, shadows and container chrome would otherwise do.")
    density = grammars["contrast"].get("density", "medium")
    if density == "high":
        out.append("The page is dense and rewards reading: specifics, numbers and detail rather "
                   "than three-word value propositions.")
    elif density == "low":
        out.append("The page is sparse and deliberate. Few elements, each given room, with "
                   "restraint doing the work that decoration would.")
    out.append(f"Read as one system, the references are {refs['near']['id']} for fit, "
               f"{refs['contrast']['id']} for contrast, {refs['outlier']['id']} for the unusual "
               f"grammar. Build in the space they bound — not a copy of any one of them.")
    return out[:4]


def _direction(grammars: dict[str, dict]) -> str:
    g = grammars["contrast"]
    bits = [
        f"{g.get('density', 'medium')}-density",
        "typography-dominant" if g.get("display_dominance", 0) >= 3 else "balanced-hierarchy",
        f"{g.get('imagery', 'present')} imagery",
        f"{g.get('geometry', 'sharp')} geometry",
        f"{g.get('section_rhythm', 'uniform')} section rhythm",
    ]
    return ", ".join(bits)


def as_markdown(contract: dict, brief: str) -> str:
    """The contract the agent writes to disk and builds against."""
    ident = contract["identity"]
    lines = [f"# DESIGN CONTRACT — {brief}", "",
             f"Direction: {ident['direction']}", "", "## Design intent", ""]
    lines += [f"- {line}" for line in ident.get("design_intent", [])]
    lines += ["", "The mandates below prevent known failure modes. The intent above is what they "
              "are for — satisfying the numbers while violating the intent is a failed build.",
              "", "## References", ""]
    for role, r in ident["references"].items():
        g = r["grammar"]
        lines.append(f"- **{role}** `{r['id']}` — {g['hero_alignment']} hero, {g['section_rhythm']} "
                     f"rhythm, {g['card_reliance']} card use, {g['geometry']} geometry, "
                     f"{g['imagery']} imagery, display dominance {g['display_dominance']}")
    lines += ["", "## Composition mandates (inherited — may not be weakened)", ""]
    for r in contract["inherited"]["required"]:
        lines.append(f"- `{r['rule']} {r['op']} {r['value']}` — {r['why']} (from {r['source']})")
    lines += ["", "## Prohibitions (inherited — may not be weakened)", ""]
    for r in contract["inherited"]["forbidden"]:
        lines.append(f"- `{r['rule']} {r['op']} {r['value']}` — {r['why']} (from {r['source']})")
    lines += ["", "## Yours to decide", ""] + [f"- {x}" for x in contract["agent_owns"]]
    lines += ["", f"> {contract['rule']}", ""]
    return "\n".join(lines)


def freeze(brief: str, build_dir: Path) -> tuple[dict, bool]:
    """Fix a selection to disk before the page exists.

    Retrieval that can be re-run after seeing the build destroys causal interpretability:
    a disappointing page gets a more convenient reference and the failure disappears. An
    existing freeze is therefore reused, never silently replaced.
    """
    build_dir = Path(build_dir)
    build_dir.mkdir(parents=True, exist_ok=True)
    path = build_dir / "contract.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8")), False

    contract = build(catalogue.select(brief))
    contract["brief"] = brief
    contract["frozen_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path.write_text(json.dumps(contract, indent=2), encoding="utf-8")
    (build_dir / "DESIGN_CONTRACT.md").write_text(as_markdown(contract, brief), encoding="utf-8")
    return contract, True


def load_frozen(build_dir: Path) -> tuple[dict | None, str]:
    path = Path(build_dir) / "contract.json"
    if not path.exists():
        return None, "none found"
    c = json.loads(path.read_text(encoding="utf-8"))
    if "inherited" not in c:  # an older freeze held only the inherited block
        c = {"inherited": c}
    refs = ", ".join(f"{role}:{r['id']}" for role, r in c.get("identity", {}).get("references", {}).items())
    return c, f"frozen {c.get('frozen_at', 'earlier')} [{refs or 'references not recorded'}]"
