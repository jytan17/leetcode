import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([3, 4, 5, 1, 2],), 1),
    (([4, 5, 6, 7, 0, 1, 2],), 0),
    (([11, 13, 15, 17],), 11),
    # Edge cases
    (([1],), 1),                         # single element
    (([2, 1],), 1),                      # two elements, rotated
    (([1, 2],), 1),                      # two elements, not rotated
    (([2, 3, 4, 5, 1],), 1),            # min at end
    (([5, 1, 2, 3, 4],), 1),            # min near start
])
def test_find_min(args, expected):
    assert Solution().findMin(*args) == expected
