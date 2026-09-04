import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([3, 1, 5, 8],), 167),
    (([1, 5],), 10),
    (([5],), 5),
])
def test_max_coins(args, expected):
    assert Solution().maxCoins(*args) == expected
