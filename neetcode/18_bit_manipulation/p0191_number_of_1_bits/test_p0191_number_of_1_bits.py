import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((11,), 3),
    ((128,), 1),
    ((2147483645,), 30),
    # Edge cases
    ((1,), 1),
    ((0,), 0),
    ((7,), 3),
    ((255,), 8),
    ((2147483647,), 31),
])
def test_hamming_weight(args, expected):
    assert Solution().hammingWeight(*args) == expected
