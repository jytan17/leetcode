import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
    (([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]]),
    # Edge cases
    (([], [5, 7]), [[5, 7]]),
    (([[1, 5]], [2, 3]), [[1, 5]]),
    (([[1, 5]], [6, 8]), [[1, 5], [6, 8]]),
    (([[2, 5], [6, 7], [8, 9]], [0, 1]), [[0, 1], [2, 5], [6, 7], [8, 9]]),
    (([[1, 5]], [0, 6]), [[0, 6]]),
])
def test_insert(args, expected):
    assert Solution().insert(*args) == expected
