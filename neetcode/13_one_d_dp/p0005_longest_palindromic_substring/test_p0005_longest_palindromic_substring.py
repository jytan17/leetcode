import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("babad",), ["bab", "aba"]),
    (("cbbd",), ["bb"]),
    # Edge cases
    (("a",), ["a"]),
    (("ac",), ["a", "c"]),
    (("racecar",), ["racecar"]),
    (("aacabdkacaa",), ["aca"]),
    (("aaaa",), ["aaaa"]),
])
def test_longest_palindrome(args, expected):
    assert Solution().longestPalindrome(*args) in expected
