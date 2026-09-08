import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([3, 1, 5, 8],), 167),
    (([1, 5],), 10),
    # Edge cases
    (([5],), 5),
    (([1],), 1),
    (([1, 2, 3],), 12),
    (([9, 76, 64, 21],), 116718),
])
def test_max_coins(args, expected):
    assert Solution().maxCoins(*args) == expected
