import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 3, 0, 2],), 3),
    (([1],), 0),
    (([2, 1],), 0),
])
def test_max_profit(args, expected):
    assert Solution().maxProfit(*args) == expected
