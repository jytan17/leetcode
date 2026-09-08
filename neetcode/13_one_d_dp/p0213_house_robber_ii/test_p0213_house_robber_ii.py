import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 3, 2],), 3),
    (([1, 2, 3, 1],), 4),
    (([1, 2, 3],), 3),
    # Edge cases
    (([1],), 1),
    (([0],), 0),
    (([1, 2],), 2),
    (([200, 3, 140, 20, 10],), 340),
])
def test_rob(args, expected):
    assert Solution().rob(*args) == expected
