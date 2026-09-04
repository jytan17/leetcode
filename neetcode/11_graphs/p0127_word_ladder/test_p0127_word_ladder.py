import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    (("a", "c", ["a", "b", "c"]), 2),
])
def test_ladder_length(args, expected):
    assert Solution().ladderLength(*args) == expected
