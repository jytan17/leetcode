import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[9, 9, 4], [6, 6, 8], [2, 1, 1]],), 4),
    (([[3, 4, 5], [3, 2, 6], [2, 2, 1]],), 4),
    (([[1]],), 1),
    # Edge cases
    (([[1, 2]],), 2),
    (([[3, 2, 1]],), 3),
    (([[1, 2], [4, 3]],), 4),
    (([[7, 8, 9], [9, 7, 6], [7, 2, 3]],), 6),
])
def test_longest_increasing_path(args, expected):
    assert Solution().longestIncreasingPath(*args) == expected
