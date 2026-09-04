import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 3, 1],), 4),
    (([2, 7, 9, 3, 1],), 12),
    (([5],), 5),
])
def test_rob(args, expected):
    assert Solution().rob(*args) == expected
