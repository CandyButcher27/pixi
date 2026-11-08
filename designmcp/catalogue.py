"""Load the annotated catalogue and pick reference triples.

Selection is deliberately not nearest-neighbour. Three adjacent references push the
agent toward the middle of the design space, which is the failure this project
exists to fix. Every query returns one near, one contrast, one outlier.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = Path(__file__).resolve().parent / "catalog.json"
LIVE_MEASURED = ROOT / "research/harvest/galleries/measured.jsonl"
LIVE_SITES = ROOT / "research/harvest/galleries/sites_merged.jsonl"

COLLECTIONS = {
    "websites": "brand homage",
    "portfolio-concepts": "original concept",
    "video_animated": "scroll-driven build",
}
CATEGORICAL = ["hero_alignment", "section_rhythm", "card_reliance", "geometry", "imagery",
               "density", "text_density"]
# field -> the spread over which a difference counts as maximal
NUMERIC = {"hero_weight_split": 0.35, "display_dominance": 4.0, "full_bleed_sections": 3.0,
           "max_radius": 32.0, "sections": 8.0}

STOPWORDS = {"a", "an", "the", "for", "of", "and", "with", "to", "in", "on", "make", "build",
             "me", "site", "website", "page", "landing", "design", "app", "web", "create"}


def live_entries(measured: Path = LIVE_MEASURED, sites: Path = LIVE_SITES) -> dict[str, dict]:
    if not measured.exists():
        return {}
    meta = {}
    if sites.exists():
        meta = {s["url"]: s for s in map(json.loads, sites.read_text(encoding="utf-8").splitlines())}
    out = {}
    for row in map(json.loads, measured.read_text(encoding="utf-8").splitlines()):
        if "grammar" not in row or "error" in row["grammar"]:
            continue
        site = meta.get(row["url"], {})
        host = row["url"].split("//", 1)[-1].strip("/")
        tags = [t.split(":", 1)[-1] for t in site.get("tags", [])]
        out[f"live:{host}"] = {"collection": "live", "path": row["url"], "grammar": row["grammar"],
                               "text": " ".join([host, *site.get("titles", []), *tags])}
    return out


def load(path: Path = CATALOG) -> dict[str, dict]:
    if not path.exists():
        raise FileNotFoundError(f"{path} missing — run scripts/annotate_designs.py first")
    return json.loads(path.read_text(encoding="utf-8"))["entries"] | live_entries()


def tokens(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", text.lower()) if len(t) > 2 and t not in STOPWORDS]


def distance(a: dict, b: dict) -> float:
    """0 = same design grammar, 1 = maximally different."""
    ga, gb = a["grammar"], b["grammar"]
    parts = []
    for f in CATEGORICAL:
        parts.append(0.0 if ga.get(f) == gb.get(f) else 1.0)
    for f, spread in NUMERIC.items():
        va, vb = ga.get(f), gb.get(f)
        if va is None or vb is None:
            continue
        parts.append(min(abs(va - vb) / spread, 1.0))
    return sum(parts) / len(parts)


def novelty(entries: dict[str, dict]) -> dict[str, float]:
    """Mean distance from each entry to the whole corpus. High = unusual grammar."""
    ids = list(entries)
    out = {}
    for i in ids:
        out[i] = sum(distance(entries[i], entries[j]) for j in ids if j != i) / max(len(ids) - 1, 1)
    return out


def relevance(brief: str, entries: dict[str, dict]) -> dict[str, float]:
    """IDF-weighted token overlap. No embeddings: 77 entries does not earn a vector store."""
    q = set(tokens(brief))
    if not q:
        return {i: 0.0 for i in entries}
    df = Counter()
    doc_tokens = {}
    for i, e in entries.items():
        toks = set(tokens(e["text"]))
        doc_tokens[i] = toks
        df.update(toks)
    n = len(entries)
    out = {}
    for i, toks in doc_tokens.items():
        score = sum(math.log(1 + n / (1 + df[t])) for t in q & toks)
        out[i] = score / math.sqrt(len(q))
    top = max(out.values()) or 1.0
    return {i: v / top for i, v in out.items()}


SEPARATION = 0.45  # a reference closer than this to an already-picked one adds nothing


def select(brief: str, entries: dict[str, dict] | None = None) -> dict[str, dict]:
    """near = fits the brief. contrast = furthest usable grammar. outlier = rarest grammar.

    Distance is a gate, not a multiplier. Multiplying relevance by distance lets a
    highly relevant but near-identical entry outscore a genuinely different one, which
    returns three adjacent references — the failure this selection exists to prevent.
    """
    entries = entries if entries is not None else load()
    rel = relevance(brief, entries)
    nov = novelty(entries)

    near_id = max(entries, key=lambda i: (rel[i], nov[i]))
    near = entries[near_id]

    def far_from(picked: list[str]):
        return [i for i in entries if i not in picked
                and min(distance(entries[p], entries[i]) for p in picked) >= SEPARATION]

    pool = far_from([near_id])
    if pool:  # most relevant design that is still structurally far from near
        contrast_id = max(pool, key=lambda i: (rel[i], nov[i]))
    else:     # clustered corpus: take the furthest thing there is
        contrast_id = max((i for i in entries if i != near_id),
                          key=lambda i: distance(near, entries[i]))

    pool = far_from([near_id, contrast_id])
    if pool:  # rarest grammar in the corpus, given it is far from both picks
        outlier_id = max(pool, key=lambda i: (nov[i], rel[i]))
    else:
        outlier_id = max((i for i in entries if i not in (near_id, contrast_id)),
                         key=lambda i: (nov[i], rel[i]))

    picks = {"near": near_id, "contrast": contrast_id, "outlier": outlier_id}
    return {
        role: dict(entries[i], id=i, role=role,
                   relevance=round(rel[i], 3), novelty=round(nov[i], 3),
                   distance_from_near=round(distance(near, entries[i]), 3))
        for role, i in picks.items()
    }


def index_lines(entries: dict[str, dict] | None = None) -> list[str]:
    """One line per entry — small enough that the agent can reason over the whole corpus."""
    entries = entries if entries is not None else load()
    lines = []
    for i in sorted(entries):
        g = entries[i]["grammar"]
        lines.append(
            f"{i} — {COLLECTIONS.get(entries[i]['collection'], entries[i]['collection'])} — "
            f"{g['hero_alignment']} hero, {g['section_rhythm']} rhythm, "
            f"{g['card_reliance']} card use, {g['geometry']} geometry, "
            f"{g['imagery']} imagery, {g['density']} density"
        )
    return lines
