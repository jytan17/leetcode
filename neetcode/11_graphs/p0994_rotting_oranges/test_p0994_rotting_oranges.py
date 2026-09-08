import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0),
    # Edge cases
    ([[2]], 0),
    ([[1]], -1),
    ([[0]], 0),
    ([[2, 1, 1, 1, 1]], 4),
    ([[2, 0, 1]], -1),
    ([[2, 2], [1, 1]], 1),
])
def test_oranges_rotting(args, expected):
    assert Solution().orangesRotting(args) == expected
