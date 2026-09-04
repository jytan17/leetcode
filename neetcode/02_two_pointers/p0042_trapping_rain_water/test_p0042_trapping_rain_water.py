import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
    (([],), 0),
    (([3, 2, 1],), 0),
])
def test_trap(args, expected):
    assert Solution().trap(*args) == expected
