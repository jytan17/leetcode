import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("aabcc", "dbbca", "aadbbcbcac"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (("", "", ""), True),
    # Edge cases
    (("a", "", "a"), True),
    (("", "b", "b"), True),
    (("a", "b", "ab"), True),
    (("a", "b", "ba"), True),
    (("a", "b", "c"), False),
    (("aa", "ab", "aaba"), True),
])
def test_is_interleave(args, expected):
    assert Solution().isInterleave(*args) == expected
