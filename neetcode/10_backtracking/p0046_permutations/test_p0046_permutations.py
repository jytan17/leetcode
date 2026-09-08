import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 3],), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    (([0, 1],), [[0, 1], [1, 0]]),
    (([1],), [[1]]),
    # Edge cases
    (([-1, 0, 1],), [[-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]]),
])
def test_permute(args, expected):
    assert sorted(map(tuple, Solution().permute(*args))) == sorted(map(tuple, expected))
