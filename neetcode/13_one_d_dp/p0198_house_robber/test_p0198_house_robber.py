import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 3, 1],), 4),
    (([2, 7, 9, 3, 1],), 12),
    # Edge cases
    (([5],), 5),
    (([1, 2],), 2),
    (([0, 0, 0],), 0),
    (([100, 1, 1, 100],), 200),
    (([2, 1, 1, 2],), 4),
])
def test_rob(args, expected):
    assert Solution().rob(*args) == expected
