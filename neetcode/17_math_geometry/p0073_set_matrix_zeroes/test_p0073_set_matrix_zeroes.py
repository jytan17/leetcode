import pytest
from solution import Solution


@pytest.mark.parametrize("matrix,expected", [
    # LeetCode examples
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    # Edge cases
    ([[1]], [[1]]),
    ([[0]], [[0]]),
    ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]),
    ([[1, 0], [0, 1]], [[0, 0], [0, 0]]),
])
def test_set_zeroes(matrix, expected):
    Solution().setZeroes(matrix)
    assert matrix == expected
