import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([10, 15, 20],), 15),
    (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
    # Edge cases
    (([0, 0],), 0),
    (([10, 15],), 10),
    (([0, 1, 2, 3],), 2),
    (([100, 1, 1, 100],), 2),
])
def test_min_cost_climbing_stairs(args, expected):
    assert Solution().minCostClimbingStairs(*args) == expected
