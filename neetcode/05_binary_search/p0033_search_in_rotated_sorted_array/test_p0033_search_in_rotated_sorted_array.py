import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
    (([3, 1], 1), 1),
])
def test_search(args, expected):
    assert Solution().search(*args) == expected
