import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 3, -2, 4],), 6),
    (([-2, 0, -1],), 0),
    # Edge cases
    (([0],), 0),
    (([-2],), -2),
    (([-2, 3, -4],), 24),
    (([2, -5, -2, -4, 3],), 24),
    (([-1, -2, -3, 0],), 6),
    (([1, 2, 3, 4],), 24),
])
def test_max_product(args, expected):
    assert Solution().maxProduct(*args) == expected
