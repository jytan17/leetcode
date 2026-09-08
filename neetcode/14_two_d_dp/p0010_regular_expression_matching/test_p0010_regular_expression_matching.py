import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("aa", "a"), False),
    (("aa", "a*"), True),
    (("ab", ".*"), True),
    (("aab", "c*a*b"), True),
    (("mississippi", "mis*is*p*."), False),
    # Edge cases
    (("", ""), True),
    (("", "a*"), True),
    (("a", ""), False),
    (("a", "a"), True),
    (("a", "."), True),
    (("ab", "a."), True),
    (("aaa", "a*a"), True),
    (("ab", ".*c"), False),
])
def test_is_match(args, expected):
    assert Solution().isMatch(*args) == expected
