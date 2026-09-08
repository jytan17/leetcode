import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    (([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),
    # Edge cases
    (([1], 1), [[1]]),
    (([1], 2), []),
    (([1, 1, 1, 1], 2), [[1, 1]]),
])
def test_combination_sum2(args, expected):
    assert sorted(sorted(x) for x in Solution().combinationSum2(*args)) == sorted(sorted(x) for x in expected)
