import pytest
from solution import Solution


INF = 2147483647


@pytest.mark.parametrize("rooms,expected", [
    # LeetCode examples
    ([[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]],
     [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
    ([[-1]], [[-1]]),
    # Edge cases
    ([[0]], [[0]]),
    ([[INF]], [[INF]]),
    ([[0, INF, INF]], [[0, 1, 2]]),
    ([[0, -1, INF]], [[0, -1, INF]]),
    ([[0, INF], [INF, INF]], [[0, 1], [1, 2]]),
])
def test_walls_and_gates(rooms, expected):
    Solution().wallsAndGates(rooms)
    assert rooms == expected
