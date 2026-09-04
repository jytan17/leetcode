import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 1, 1, 1, 1], 3), 5),
    (([1], 1), 1),
    (([1], 2), 0),
])
def test_find_target_sum_ways(args, expected):
    assert Solution().findTargetSumWays(*args) == expected
