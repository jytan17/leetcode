import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 3, 1, 1, 4],), True),
    (([3, 2, 1, 0, 4],), False),
    (([0],), True),
])
def test_can_jump(args, expected):
    assert Solution().canJump(*args) == expected
