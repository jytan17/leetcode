import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
    (([1],), 0),
])
def test_max_profit(args, expected):
    assert Solution().maxProfit(*args) == expected
