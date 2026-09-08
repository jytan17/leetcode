import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    (([1],), 1),
    (([5, 4, -1, 7, 8],), 23),
    # Edge cases
    (([-3, -2, -5],), -2),
    (([-1],), -1),
    (([0, -1, 0],), 0),
    (([1, 2, 3, 4, 5],), 15),
])
def test_max_sub_array(args, expected):
    assert Solution().maxSubArray(*args) == expected
