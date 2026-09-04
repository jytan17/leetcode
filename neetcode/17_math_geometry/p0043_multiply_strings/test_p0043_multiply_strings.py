import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("2", "3"), "6"),
    (("123", "456"), "56088"),
    (("0", "0"), "0"),
    (("9", "99"), "891"),
])
def test_multiply(args, expected):
    assert Solution().multiply(*args) == expected
