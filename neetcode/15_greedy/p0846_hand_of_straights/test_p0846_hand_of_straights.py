import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
    (([1, 2, 3, 4, 5], 4), False),
    # Edge cases
    (([1], 1), True),
    (([1, 2, 3], 1), True),
    (([1, 1, 2, 2, 3, 3], 3), True),
    (([1, 2, 3, 4], 2), True),
    (([1, 3, 5, 7], 2), False),
])
def test_is_n_straight_hand(args, expected):
    assert Solution().isNStraightHand(*args) == expected
