import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"), "a"),
    (("a", "aa"), ""),
])
def test_min_window(args, expected):
    assert Solution().minWindow(*args) == expected
