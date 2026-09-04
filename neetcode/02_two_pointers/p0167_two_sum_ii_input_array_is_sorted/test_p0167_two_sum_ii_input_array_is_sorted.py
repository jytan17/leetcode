import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2]),
])
def test_two_sum(args, expected):
    assert Solution().twoSum(*args) == expected
