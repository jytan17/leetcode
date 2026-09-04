import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    (([1, 1],), 1),
    (([2, 3, 4, 5, 18, 17, 6],), 17),
])
def test_max_area(args, expected):
    assert Solution().maxArea(*args) == expected
