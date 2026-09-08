import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]), True),
    (([[3, 4, 5], [4, 5, 6]], [3, 2, 5]), False),
    (([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]), True),
    # Edge cases
    (([[1, 1, 1]], [1, 1, 1]), True),
    (([[1, 2, 3]], [1, 2, 4]), False),
    (([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [3, 3, 3]), True),
])
def test_merge_triplets(args, expected):
    assert Solution().mergeTriplets(*args) == expected
