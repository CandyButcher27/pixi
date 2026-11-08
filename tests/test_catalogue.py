import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from designmcp.catalogue import live_entries  # noqa: E402


def test_live_entries_keep_only_measured_rows_with_gallery_text(tmp_path):
    measured = tmp_path / "measured.jsonl"
    sites = tmp_path / "sites.jsonl"
    rows = [
        {"url": "https://a.studio/", "grammar": {"hero_alignment": "left"}},
        {"url": "https://dead.site", "error": "Error: net::ERR_NAME_NOT_RESOLVED"},
        {"url": "https://blank.page", "grammar": {"error": "no sections"}},
    ]
    measured.write_text("\n".join(map(json.dumps, rows)), encoding="utf-8")
    sites.write_text(json.dumps({"url": "https://a.studio/", "titles": ["A Studio"],
                                 "tags": ["awwwards/tag:brutalist"]}), encoding="utf-8")

    out = live_entries(measured, sites)

    assert list(out) == ["live:a.studio"]
    entry = out["live:a.studio"]
    assert entry["collection"] == "live"
    assert entry["path"] == "https://a.studio/"
    assert entry["text"] == "a.studio A Studio brutalist"


def test_live_entries_empty_without_harvest(tmp_path):
    assert live_entries(tmp_path / "missing.jsonl", tmp_path / "missing2.jsonl") == {}


def test_outlier_prefers_relevant_rare_grammar_over_rarest():
    from designmcp.catalogue import CATEGORICAL, select

    def entry(text, *vals):
        return {"collection": "websites", "path": "", "text": text,
                "grammar": dict(zip(CATEGORICAL, vals))}

    common = ("x",) * 7
    entries = {f"c{i}": entry("filler", *common) for i in range(1, 6)}
    entries["c0"] = entry("ramen noodle broth", *common)
    entries["fits"] = entry("broth", *("a",) * 4, *("x",) * 3)
    entries["contrast"] = entry("noodle ramen", *("b",) * 4, *("x",) * 3)
    entries["rarest"] = entry("unrelated", *("z",) * 7)

    picks = select("ramen noodle broth", entries)

    assert [picks[r]["id"] for r in ("near", "contrast", "outlier")] == ["c0", "contrast", "fits"]
