import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 3, 1, 1, 4],), True),
    (([3, 2, 1, 0, 4],), False),
    # Edge cases
    (([0],), True),
    (([1, 0],), True),
    (([0, 1],), False),
    (([1, 1, 1, 1, 1],), True),
    (([5, 0, 0, 0, 0],), True),
])
def test_can_jump(args, expected):
    assert Solution().canJump(*args) == expected
