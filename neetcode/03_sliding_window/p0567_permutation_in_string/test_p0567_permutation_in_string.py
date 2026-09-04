import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("ab", "eidbaooo"), True),
    (("ab", "eidboaoo"), False),
    (("abc", "ab"), False),
])
def test_check_inclusion(args, expected):
    assert Solution().checkInclusion(*args) == expected
