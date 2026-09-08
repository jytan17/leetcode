import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((2,), 2),
    ((3,), 3),
    # Edge cases
    ((1,), 1),
    ((4,), 5),
    ((5,), 8),
    ((10,), 89),
    ((45,), 1836311903),
])
def test_climb_stairs(args, expected):
    assert Solution().climbStairs(*args) == expected
