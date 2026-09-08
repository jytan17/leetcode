import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((123,), 321),
    ((-123,), -321),
    ((120,), 21),
    # Edge cases
    ((0,), 0),
    ((1534236469,), 0),
    ((-2147483648,), 0),
    ((2147483647,), 0),
    ((10,), 1),
    ((-10,), -1),
])
def test_reverse(args, expected):
    assert Solution().reverse(*args) == expected
