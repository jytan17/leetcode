import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 2, 1],), 1),
    (([4, 1, 2, 1, 2],), 4),
    (([1],), 1),
    # Edge cases
    (([0, 1, 0],), 1),
    (([-1, -1, -2],), -2),
    (([100, 200, 100],), 200),
])
def test_single_number(args, expected):
    assert Solution().singleNumber(*args) == expected
