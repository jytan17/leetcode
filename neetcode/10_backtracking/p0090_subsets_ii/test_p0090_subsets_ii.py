import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 2],), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    (([0],), [[], [0]]),
    # Edge cases
    (([1, 1, 1],), [[], [1], [1, 1], [1, 1, 1]]),
    (([3, 1, 1],), [[], [1], [1, 1], [1, 1, 3], [1, 3], [3]]),
    (([4, 4, 1, 4],), [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [4], [4, 4], [4, 4, 4]]),
])
def test_subsets_with_dup(args, expected):
    assert sorted(sorted(x) for x in Solution().subsetsWithDup(*args)) == sorted(sorted(x) for x in expected)
