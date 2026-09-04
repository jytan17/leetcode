import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],), 20),
    (([[3, 12], [-2, 5], [-4, 1]],), 18),
    (([[0, 0]],), 0),
])
def test_min_cost_connect_points(args, expected):
    assert Solution().minCostConnectPoints(*args) == expected
