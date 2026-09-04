import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[1, 2], [2, 3], [3, 4], [1, 3]],), 1),
    (([[1, 2], [1, 2], [1, 2]],), 2),
    (([[1, 2], [2, 3]],), 0),
])
def test_erase_overlap_intervals(args, expected):
    assert Solution().eraseOverlapIntervals(*args) == expected
