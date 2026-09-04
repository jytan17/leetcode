import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((19,), True),
    ((2,), False),
    ((1,), True),
    ((7,), True),
])
def test_is_happy(args, expected):
    assert Solution().isHappy(*args) == expected
