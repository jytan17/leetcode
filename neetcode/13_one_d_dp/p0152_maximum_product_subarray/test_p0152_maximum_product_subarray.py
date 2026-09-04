import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 3, -2, 4],), 6),
    (([-2, 0, -1],), 0),
    (([-2],), -2),
    (([-2, 3, -4],), 24),
])
def test_max_product(args, expected):
    assert Solution().maxProduct(*args) == expected
