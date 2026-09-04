import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[9, 9, 4], [6, 6, 8], [2, 1, 1]],), 4),
    (([[3, 4, 5], [3, 2, 6], [2, 2, 1]],), 4),
    (([[1]],), 1),
])
def test_longest_increasing_path(args, expected):
    assert Solution().longestIncreasingPath(*args) == expected
