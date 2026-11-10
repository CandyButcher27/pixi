import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from blind import tally  # noqa: E402


def test_tally_maps_screen_side_back_to_arm():
    rows = [
        {"left": "treatment", "right": "control", "choice": "left"},
        {"left": "control", "right": "treatment", "choice": "left"},
        {"left": "control", "right": "treatment", "choice": "right"},
        {"left": "treatment", "right": "control", "choice": "tie"},
        {"left": "control", "right": "treatment", "choice": "both_generic"},
    ]
    assert tally(rows) == {"treatment": 2, "control": 1, "tie": 1, "both_generic": 1}
