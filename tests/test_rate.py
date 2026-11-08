import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from rate import pick_pair  # noqa: E402


def test_pick_pair_stays_within_page_type_and_skips_rated():
    pool = {"pricing": ["a", "b", "c"], "docs": ["x", "y"]}
    seen = {frozenset(("x", "y")), frozenset(("a", "b")), frozenset(("a", "c"))}
    for _ in range(50):
        page_type, left, right = pick_pair(pool, seen, random.Random())
        assert {left, right} <= set(pool[page_type])
        assert left != right
        assert frozenset((left, right)) not in seen
        assert frozenset((left, right)) == frozenset(("b", "c"))


def test_pick_pair_raises_when_everything_rated():
    pool = {"docs": ["x", "y"]}
    with pytest.raises(RuntimeError):
        pick_pair(pool, {frozenset(("x", "y"))}, random.Random(0))
