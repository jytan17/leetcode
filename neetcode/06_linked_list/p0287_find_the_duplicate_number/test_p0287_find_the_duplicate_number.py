import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 3, 4, 2, 2],), 2),
    (([3, 1, 3, 4, 2],), 3),
    (([3, 3, 3, 3, 3],), 3),
    # Edge cases
    (([1, 1],), 1),
    (([2, 2, 2, 2, 2],), 2),
    (([1, 4, 4, 2, 4],), 4),
    (([1, 2, 3, 4, 5, 3],), 3),
])
def test_find_duplicate(args, expected):
    assert Solution().findDuplicate(*args) == expected
