import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 1, 5, 6, 2, 3],), 10),
    (([2, 4],), 4),
    # Edge: single bar
    (([1],), 1),
    # Edge: all same height
    (([3, 3, 3, 3],), 12),
    # Edge: strictly increasing
    (([1, 2, 3, 4, 5],), 9),
    # Edge: strictly decreasing
    (([5, 4, 3, 2, 1],), 9),
    # Edge: contains zero
    (([2, 0, 2],), 2),
    # Edge: tall single bar
    (([0, 9, 0],), 9),
])
def test_largest_rectangle_area(args, expected):
    assert Solution().largestRectangleArea(*args) == expected
