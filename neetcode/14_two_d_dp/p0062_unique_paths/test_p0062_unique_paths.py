import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((3, 7), 28),
    ((3, 2), 3),
    # Edge cases
    ((1, 1), 1),
    ((1, 10), 1),
    ((10, 1), 1),
    ((2, 2), 2),
    ((7, 3), 28),
    ((10, 10), 48620),
])
def test_unique_paths(args, expected):
    assert Solution().uniquePaths(*args) == expected
