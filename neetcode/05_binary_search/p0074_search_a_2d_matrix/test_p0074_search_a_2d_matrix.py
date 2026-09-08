import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
    # Edge cases
    (([[1]], 1), True),                  # 1x1 matrix, found
    (([[1]], 2), False),                 # 1x1 matrix, not found
    (([[1, 3, 5, 7]], 7), True),         # single row, last element
    (([[1], [3], [5]], 3), True),        # single column
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1), True),   # first element
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60), True),  # last element
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0), False),  # smaller than all
])
def test_search_matrix(args, expected):
    assert Solution().searchMatrix(*args) == expected
