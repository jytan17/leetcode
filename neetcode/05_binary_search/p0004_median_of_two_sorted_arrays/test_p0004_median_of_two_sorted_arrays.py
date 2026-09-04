import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 3], [2]), 2.0),
    (([1, 2], [3, 4]), 2.5),
    (([], [1]), 1.0),
    (([2], []), 2.0),
])
def test_find_median_sorted_arrays(args, expected):
    assert Solution().findMedianSortedArrays(*args) == pytest.approx(expected)
