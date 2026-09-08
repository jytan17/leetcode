import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 7, 4, 1, 8, 1],), 1),
    (([1],), 1),
    # Edge cases
    (([2, 2],), 0),
    (([3, 7, 2],), 2),
    (([10, 10, 10, 10],), 0),
    (([1, 1, 1],), 1),
])
def test_last_stone_weight(args, expected):
    assert Solution().lastStoneWeight(*args) == expected
