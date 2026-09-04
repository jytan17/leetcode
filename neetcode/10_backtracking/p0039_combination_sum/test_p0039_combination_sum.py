import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
    (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    (([2], 1), []),
])
def test_combination_sum(args, expected):
    assert sorted(sorted(x) for x in Solution().combinationSum(*args)) == sorted(sorted(x) for x in expected)
