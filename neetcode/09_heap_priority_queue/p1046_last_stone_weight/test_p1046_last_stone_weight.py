import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 7, 4, 1, 8, 1],), 1),
    (([1],), 1),
    (([2, 2],), 0),
])
def test_last_stone_weight(args, expected):
    assert Solution().lastStoneWeight(*args) == expected
