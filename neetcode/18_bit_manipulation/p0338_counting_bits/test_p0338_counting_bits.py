import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((2,), [0, 1, 1]),
    ((5,), [0, 1, 1, 2, 1, 2]),
    ((0,), [0]),
])
def test_count_bits(args, expected):
    assert Solution().countBits(*args) == expected
