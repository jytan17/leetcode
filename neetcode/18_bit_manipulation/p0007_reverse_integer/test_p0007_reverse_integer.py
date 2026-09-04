import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((123,), 321),
    ((-123,), -321),
    ((120,), 21),
    ((1534236469,), 0),
    ((0,), 0),
])
def test_reverse(args, expected):
    assert Solution().reverse(*args) == expected
