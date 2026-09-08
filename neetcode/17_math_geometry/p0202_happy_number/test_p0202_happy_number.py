import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((19,), True),
    ((2,), False),
    # Edge cases
    ((1,), True),
    ((7,), True),
    ((4,), False),
    ((100,), True),
    ((116,), False),
])
def test_is_happy(args, expected):
    assert Solution().isHappy(*args) == expected
