import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((2,), 2),
    ((3,), 3),
    ((1,), 1),
    ((5,), 8),
])
def test_climb_stairs(args, expected):
    assert Solution().climbStairs(*args) == expected
