import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 3], [2]), 2.0),
    (([1, 2], [3, 4]), 2.5),
    # Edge cases
    (([], [1]), 1.0),                    # first array empty
    (([2], []), 2.0),                    # second array empty
    (([1, 2], [1, 2]), 1.5),             # identical arrays
    (([1], [2, 3, 4, 5, 6]), 3.5),       # very different lengths
    (([1, 2, 3], [4, 5, 6]), 3.5),       # no overlap
    (([3], [1, 2]), 2.0),                # single vs pair
    (([1, 3], [2, 4, 5, 6]), 3.5),       # interleaved
])
def test_find_median_sorted_arrays(args, expected):
    assert Solution().findMedianSortedArrays(*args) == pytest.approx(expected)
