import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((2.00000, 10), 1024.00000),
    ((2.10000, 3), 9.26100),
    ((2.00000, -2), 0.25000),
    ((1.0, 0), 1.0),
])
def test_my_pow(args, expected):
    assert Solution().myPow(*args) == pytest.approx(expected)
