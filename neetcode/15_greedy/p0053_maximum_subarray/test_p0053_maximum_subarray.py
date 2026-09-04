import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    (([1],), 1),
    (([5, 4, -1, 7, 8],), 23),
    (([-3, -2, -5],), -2),
])
def test_max_sub_array(args, expected):
    assert Solution().maxSubArray(*args) == expected
