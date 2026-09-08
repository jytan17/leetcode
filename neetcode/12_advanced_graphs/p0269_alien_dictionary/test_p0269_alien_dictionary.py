import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["z", "x"], "zx"),
    (["z", "x", "z"], ""),
    # Edge cases
    (["abc", "ab"], ""),
    (["z"], "z"),
    (["ab", "abc"], "abc"),
    (["a", "b", "c"], "abc"),
])
def test_alien_order(args, expected):
    result = Solution().alienOrder(args)
    if expected == "":
        assert result == ""
    else:
        assert set(result) == set(expected)
        assert len(result) == len(expected)
