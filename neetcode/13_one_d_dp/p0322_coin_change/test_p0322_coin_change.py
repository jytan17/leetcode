import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0),
    # Edge cases
    (([1], 1), 1),
    (([1], 2), 2),
    (([2], 4), 2),
    (([1, 5, 10, 25], 30), 2),
    (([186, 419, 83, 408], 6249), 20),
])
def test_coin_change(args, expected):
    assert Solution().coinChange(*args) == expected
