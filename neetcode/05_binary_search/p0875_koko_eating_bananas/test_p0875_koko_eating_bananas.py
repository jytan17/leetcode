import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([3, 6, 7, 11], 8), 4),
    (([30, 11, 23, 4, 20], 5), 30),
    (([30, 11, 23, 4, 20], 6), 23),
    # Edge cases
    (([1], 1), 1),                       # single pile, exact hours
    (([1000000000], 2), 500000000),      # large pile, two hours
    (([2, 2], 2), 2),                    # equal piles, exact hours
    (([1, 1, 1, 1], 4), 1),             # all ones, exact hours
    (([312884470], 312884469), 2),       # near max hours
])
def test_min_eating_speed(args, expected):
    assert Solution().minEatingSpeed(*args) == expected
