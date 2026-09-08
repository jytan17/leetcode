import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
    # Edge cases
    (([0],), 0),
    (([1, 1, 1, 1],), 3),
    (([10, 0, 0, 0, 0],), 1),
    (([1, 2, 3],), 2),
])
def test_jump(args, expected):
    assert Solution().jump(*args) == expected
