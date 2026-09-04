import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((1, 2), 3),
    ((2, 3), 5),
    ((-1, 1), 0),
    ((-2, -3), -5),
])
def test_get_sum(args, expected):
    assert Solution().getSum(*args) == expected
