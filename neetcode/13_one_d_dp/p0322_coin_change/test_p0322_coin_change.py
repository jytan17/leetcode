import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 5], 11), 3),
    (([2], 3), -1),
    (([1], 0), 0),
    (([2], 4), 2),
])
def test_coin_change(args, expected):
    assert Solution().coinChange(*args) == expected
