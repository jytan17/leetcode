import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]), [3, 3, 1, 4]),
    (([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]), [2, -1, 4, 6]),
    # Edge cases
    (([[1, 1]], [1]), [1]),
    (([[1, 5]], [6]), [-1]),
    (([[1, 3], [2, 4]], [2, 2]), [3, 3]),
    (([[1, 10]], [1, 5, 10]), [10, 10, 10]),
])
def test_min_interval(args, expected):
    assert Solution().minInterval(*args) == expected
