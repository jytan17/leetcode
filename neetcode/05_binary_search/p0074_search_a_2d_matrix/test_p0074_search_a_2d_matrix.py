import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
    (([[1]], 1), True),
])
def test_search_matrix(args, expected):
    assert Solution().searchMatrix(*args) == expected
