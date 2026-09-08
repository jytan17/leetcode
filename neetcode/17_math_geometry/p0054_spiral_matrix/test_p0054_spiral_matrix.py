import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    # Edge cases
    (([[7]],), [7]),
    (([[1, 2, 3]],), [1, 2, 3]),
    (([[1], [2], [3]],), [1, 2, 3]),
    (([[1, 2], [3, 4]],), [1, 2, 4, 3]),
])
def test_spiral_order(args, expected):
    assert Solution().spiralOrder(*args) == expected
