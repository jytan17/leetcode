import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 3, 2],), 3),
    (([1, 2, 3, 1],), 4),
    (([1, 2, 3],), 3),
    (([1],), 1),
])
def test_rob(args, expected):
    assert Solution().rob(*args) == expected
