import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from pixi_check import flash_rate, flashes  # noqa: E402


def test_blinking_caret_at_one_hertz_is_not_a_flash():
    assert flash_rate([1, 0, 1], 1000) == 1.0
    assert flashes([{"name": "blink", "duration": 1000, "iterations": float("inf"), "opacity": [1, 0, 1]}]) == []


def test_fast_opacity_loop_is_flagged():
    assert flashes([{"name": "strobe", "duration": 200, "iterations": float("inf"), "opacity": [1, 0, 1]}]) == ["strobe 5.0/s"]


def test_small_swings_and_one_shot_fades_are_ignored():
    assert flash_rate([1, 0.8, 1], 100) == 0.0
    assert flashes([{"name": "fade", "duration": 100, "iterations": 1, "opacity": [0, 1]}]) == []
