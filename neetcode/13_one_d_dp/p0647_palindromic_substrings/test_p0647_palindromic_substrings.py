import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("abc",), 3),
    (("aaa",), 6),
    # Edge cases
    (("a",), 1),
    (("ab",), 2),
    (("aba",), 4),
    (("abba",), 6),
])
def test_count_substrings(args, expected):
    assert Solution().countSubstrings(*args) == expected
