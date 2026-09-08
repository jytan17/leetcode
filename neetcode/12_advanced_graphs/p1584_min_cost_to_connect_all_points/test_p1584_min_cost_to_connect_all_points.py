import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
    ([[3, 12], [-2, 5], [-4, 1]], 18),
    # Edge cases
    ([[0, 0]], 0),
    ([[0, 0], [1, 1]], 2),
    ([[0, 0], [1, 0], [0, 1], [1, 1]], 3),
    ([[-1000000, -1000000], [1000000, 1000000]], 4000000),
])
def test_min_cost_connect_points(args, expected):
    assert Solution().minCostConnectPoints(args) == expected
