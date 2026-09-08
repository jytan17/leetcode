import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("2", "3"), "6"),
    (("123", "456"), "56088"),
    # Edge cases
    (("0", "0"), "0"),
    (("0", "12345"), "0"),
    (("9", "99"), "891"),
    (("999", "999"), "998001"),
    (("1", "1"), "1"),
])
def test_multiply(args, expected):
    assert Solution().multiply(*args) == expected
