import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((5, [1, 2, 5]), 4),
    ((3, [2]), 0),
    ((10, [10]), 1),
    # Edge cases
    ((0, [7]), 1),
    ((1, [1]), 1),
    ((100, [1, 5, 10, 25]), 242),
    ((5, [1]), 1),
])
def test_change(args, expected):
    assert Solution().change(*args) == expected
