import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    (([5], 5), 0),
    (([5], -5), -1),
])
def test_search(args, expected):
    assert Solution().search(*args) == expected
