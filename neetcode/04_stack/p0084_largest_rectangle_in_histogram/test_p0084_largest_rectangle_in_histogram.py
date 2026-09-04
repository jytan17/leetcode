import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 1, 5, 6, 2, 3],), 10),
    (([2, 4],), 4),
    (([1],), 1),
])
def test_largest_rectangle_area(args, expected):
    assert Solution().largestRectangleArea(*args) == expected
