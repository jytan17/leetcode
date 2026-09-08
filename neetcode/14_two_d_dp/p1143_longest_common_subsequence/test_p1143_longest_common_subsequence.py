import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("abcde", "ace"), 3),
    (("abc", "abc"), 3),
    (("abc", "def"), 0),
    # Edge cases
    (("a", "a"), 1),
    (("a", "b"), 0),
    (("oxcpqrsvwf", "shmtulqrypy"), 2),
    (("bsbininm", "jmjkbkjkv"), 1),
])
def test_longest_common_subsequence(args, expected):
    assert Solution().longestCommonSubsequence(*args) == expected
