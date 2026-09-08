import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    # Edge cases
    (([5], 5), 0),
    (([5], -5), -1),
    (([-1, 0, 3, 5, 9, 12], -1), 0),   # target is first element
    (([-1, 0, 3, 5, 9, 12], 12), 5),   # target is last element
    (([1, 2], 1), 0),                   # two elements, find first
    (([1, 2], 2), 1),                   # two elements, find second
    (([1, 2], 3), -1),                  # two elements, not found
])
def test_search(args, expected):
    assert Solution().search(*args) == expected
