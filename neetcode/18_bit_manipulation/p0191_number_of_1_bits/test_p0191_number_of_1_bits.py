import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((11,), 3),
    ((128,), 1),
    ((2147483645,), 30),
    ((1,), 1),
])
def test_hamming_weight(args, expected):
    assert Solution().hammingWeight(*args) == expected
