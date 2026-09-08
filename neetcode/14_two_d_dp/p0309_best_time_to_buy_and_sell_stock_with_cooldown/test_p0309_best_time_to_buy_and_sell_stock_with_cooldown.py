import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 3, 0, 2],), 3),
    (([1],), 0),
    # Edge cases
    (([2, 1],), 0),
    (([1, 2],), 1),
    (([1, 2, 4],), 3),
    (([6, 1, 3, 2, 4, 7],), 6),
    (([1, 4, 2],), 3),
])
def test_max_profit(args, expected):
    assert Solution().maxProfit(*args) == expected
