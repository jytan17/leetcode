import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
    ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
    # Edge cases
    ([[1]], 1),
    ([[0]], 0),
    ([[1, 1], [1, 0]], 3),
    ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 1),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]], 9),
])
def test_max_area_of_island(args, expected):
    assert Solution().maxAreaOfIsland(args) == expected
