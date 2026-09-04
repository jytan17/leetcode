import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("babad",), ["bab", "aba"]),
    (("cbbd",), ["bb"]),
    (("a",), ["a"]),
    (("ac",), ["a", "c"]),
])
def test_longest_palindrome(args, expected):
    assert Solution().longestPalindrome(*args) in expected
