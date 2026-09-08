import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 3],), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    (([0],), [[], [0]]),
    # Edge cases
    (([1, 2],), [[], [1], [2], [1, 2]]),
    (([-1, 0, 1],), [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]),
])
def test_subsets(args, expected):
    assert sorted(sorted(x) for x in Solution().subsets(*args)) == sorted(sorted(x) for x in expected)
