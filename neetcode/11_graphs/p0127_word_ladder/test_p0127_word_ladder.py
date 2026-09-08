import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    # Edge cases
    (("a", "c", ["a", "b", "c"]), 2),
    (("hot", "dog", ["hot", "dog"]), 0),
    (("hot", "dog", ["hot", "dot", "dog"]), 3),
    (("hit", "hit", ["hit"]), 0),
])
def test_ladder_length(args, expected):
    assert Solution().ladderLength(*args) == expected
