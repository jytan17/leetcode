import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("abc",), 3),
    (("aaa",), 6),
    (("a",), 1),
])
def test_count_substrings(args, expected):
    assert Solution().countSubstrings(*args) == expected
