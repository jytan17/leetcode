import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 1, 1, 1, 1], 3), 5),
    (([1], 1), 1),
    # Edge cases
    (([1], 2), 0),
    (([0, 0, 0, 0, 0], 0), 32),
    (([1, 0], 1), 2),
    (([2, 1], 1), 1),
    (([1, 2, 1], 0), 2),
])
def test_find_target_sum_ways(args, expected):
    assert Solution().findTargetSumWays(*args) == expected
