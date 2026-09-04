import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1), 700),
    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), 200),
    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500),
])
def test_find_cheapest_price(args, expected):
    assert Solution().findCheapestPrice(*args) == expected
