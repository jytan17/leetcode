import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((1, 2), 3),
    ((2, 3), 5),
    # Edge cases
    ((-1, 1), 0),
    ((-2, -3), -5),
    ((0, 0), 0),
    ((0, 5), 5),
    ((-1000, 1000), 0),
    ((100, -100), 0),
])
def test_get_sum(args, expected):
    assert Solution().getSum(*args) == expected
