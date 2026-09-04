import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 3, 4, 2, 2],), 2),
    (([3, 1, 3, 4, 2],), 3),
    (([3, 3, 3, 3, 3],), 3),
    (([1, 1],), 1),
])
def test_find_duplicate(args, expected):
    assert Solution().findDuplicate(*args) == expected
