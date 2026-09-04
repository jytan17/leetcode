import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("aabcc", "dbbca", "aadbbcbcac"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (("", "", ""), True),
    (("a", "", "a"), True),
])
def test_is_interleave(args, expected):
    assert Solution().isInterleave(*args) == expected
