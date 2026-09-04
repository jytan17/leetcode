import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((5, [1, 2, 5]), 4),
    ((3, [2]), 0),
    ((10, [10]), 1),
    ((0, [7]), 1),
])
def test_change(args, expected):
    assert Solution().change(*args) == expected
