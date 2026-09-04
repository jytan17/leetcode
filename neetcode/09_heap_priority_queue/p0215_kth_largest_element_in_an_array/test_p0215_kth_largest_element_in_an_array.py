import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    (([1], 1), 1),
])
def test_find_kth_largest(args, expected):
    assert Solution().findKthLargest(*args) == expected
