import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
    (([1, 2, 3, 4, 5], 4), False),
    (([1], 1), True),
])
def test_is_n_straight_hand(args, expected):
    assert Solution().isNStraightHand(*args) == expected
