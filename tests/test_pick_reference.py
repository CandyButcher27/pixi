import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import pick_reference  # noqa: E402


def test_feel_candidates_skip_missing_screenshots(tmp_path, monkeypatch):
    shots = tmp_path / "screens"
    shots.mkdir()
    (shots / "here.png").write_bytes(b"png")
    feels = tmp_path / "feels.json"
    feels.write_text(json.dumps({"picks": {
        "here.com": {"url": "https://here.com", "feels": ["clean"], "shot": "screens/here.png"},
        "gone.com": {"url": "https://gone.com", "feels": ["clean"], "shot": "screens/gone.png"},
        "seed:x": {"url": "file:///x.png", "feels": ["clean"], "shot": "screens/here.png"},
    }}), encoding="utf-8")
    monkeypatch.setattr(pick_reference, "FEELS", feels)
    monkeypatch.setattr(pick_reference, "SHOTS", shots)
    monkeypatch.setattr(pick_reference, "FABLE", tmp_path / "no-fable")
    found = pick_reference.feel_candidates("coffee", "clean", {})
    assert [c["url"] for c in found] == ["https://here.com"]
