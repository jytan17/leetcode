import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 5, 11, 5],), True),
    (([1, 2, 3, 5],), False),
    # Edge cases
    (([1, 1],), True),
    (([1],), False),
    (([2, 2, 1, 1],), True),
    (([1, 2, 5],), False),
    (([100, 100, 100, 100, 100, 100, 100, 100],), True),
    (([1, 2, 3, 4, 5, 6, 7],), True),
])
def test_can_partition(args, expected):
    assert Solution().canPartition(*args) == expected
