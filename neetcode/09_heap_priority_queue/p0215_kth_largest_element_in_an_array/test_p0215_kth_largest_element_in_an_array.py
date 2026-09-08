import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    # Edge cases
    (([1], 1), 1),
    (([2, 1], 1), 2),
    (([2, 1], 2), 1),
    (([7, 7, 7, 7], 2), 7),
    (([99, 99], 1), 99),
])
def test_find_kth_largest(args, expected):
    assert Solution().findKthLargest(*args) == expected
