import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
    # Edge cases
    (([1], 1), 0),                       # single element, found
    (([3, 1], 1), 1),                    # two elements, find second
    (([3, 1], 3), 0),                    # two elements, find first
    (([4, 5, 6, 7, 0, 1, 2], 4), 0),    # target is first element
    (([4, 5, 6, 7, 0, 1, 2], 2), 6),    # target is last element
    (([1, 2, 3, 4, 5], 3), 2),          # not rotated
])
def test_search(args, expected):
    assert Solution().search(*args) == expected
