import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((43261596,), 964176192),
    ((4294967293,), 3221225471),
    # Edge cases
    ((0,), 0),
    ((1,), 2147483648),
    ((4294967295,), 4294967295),
    ((2147483648,), 1),
])
def test_reverse_bits(args, expected):
    assert Solution().reverseBits(*args) == expected
