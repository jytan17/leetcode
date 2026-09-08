import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[1, 2], [2, 3], [3, 4], [1, 3]],), 1),
    (([[1, 2], [1, 2], [1, 2]],), 2),
    (([[1, 2], [2, 3]],), 0),
    # Edge cases
    (([[0, 1]],), 0),
    (([[1, 100], [11, 22], [1, 11], [2, 12]],), 2),
    (([[-1, 0], [0, 1], [-1, 1]],), 1),
])
def test_erase_overlap_intervals(args, expected):
    assert Solution().eraseOverlapIntervals(*args) == expected
