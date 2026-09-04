import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((43261596,), 964176192),
    ((4294967293,), 3221225471),
    ((0,), 0),
    ((1,), 2147483648),
])
def test_reverse_bits(args, expected):
    assert Solution().reverseBits(*args) == expected
