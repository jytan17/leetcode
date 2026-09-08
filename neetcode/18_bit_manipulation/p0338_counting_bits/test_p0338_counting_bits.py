import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((2,), [0, 1, 1]),
    ((5,), [0, 1, 1, 2, 1, 2]),
    # Edge cases
    ((0,), [0]),
    ((1,), [0, 1]),
    ((8,), [0, 1, 1, 2, 1, 2, 2, 3, 1]),
])
def test_count_bits(args, expected):
    assert Solution().countBits(*args) == expected
