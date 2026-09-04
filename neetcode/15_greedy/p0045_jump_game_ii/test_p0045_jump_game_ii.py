import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
    (([0],), 0),
])
def test_jump(args, expected):
    assert Solution().jump(*args) == expected
