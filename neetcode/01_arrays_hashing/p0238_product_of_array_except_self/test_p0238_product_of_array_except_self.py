import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 3, 4],), [24, 12, 8, 6]),
    (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    (([0, 0],), [0, 0]),
])
def test_product_except_self(args, expected):
    assert Solution().productExceptSelf(*args) == expected
