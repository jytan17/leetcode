import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("aa", "a"), False),
    (("aa", "a*"), True),
    (("ab", ".*"), True),
    (("aab", "c*a*b"), True),
    (("mississippi", "mis*is*p*."), False),
])
def test_is_match(args, expected):
    assert Solution().isMatch(*args) == expected
