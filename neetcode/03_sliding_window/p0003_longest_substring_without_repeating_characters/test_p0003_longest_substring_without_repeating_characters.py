import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
    (("",), 0),
])
def test_length_of_longest_substring(args, expected):
    assert Solution().lengthOfLongestSubstring(*args) == expected
