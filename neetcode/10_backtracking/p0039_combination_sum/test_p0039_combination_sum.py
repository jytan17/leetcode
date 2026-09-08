import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
    (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    (([2], 1), []),
    # Edge cases
    (([1], 1), [[1]]),
    (([1], 3), [[1, 1, 1]]),
    (([3, 5, 7], 11), [[3, 3, 5]]),
])
def test_combination_sum(args, expected):
    assert sorted(sorted(x) for x in Solution().combinationSum(*args)) == sorted(sorted(x) for x in expected)
