import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("abcde", "ace"), 3),
    (("abc", "abc"), 3),
    (("abc", "def"), 0),
])
def test_longest_common_subsequence(args, expected):
    assert Solution().longestCommonSubsequence(*args) == expected
