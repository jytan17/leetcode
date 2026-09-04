import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 5, 11, 5],), True),
    (([1, 2, 3, 5],), False),
    (([1, 1],), True),
    (([1],), False),
])
def test_can_partition(args, expected):
    assert Solution().canPartition(*args) == expected
