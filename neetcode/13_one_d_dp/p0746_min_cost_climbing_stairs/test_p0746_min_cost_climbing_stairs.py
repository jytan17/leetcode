import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([10, 15, 20],), 15),
    (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
    (([0, 0],), 0),
])
def test_min_cost_climbing_stairs(args, expected):
    assert Solution().minCostClimbingStairs(*args) == expected
