import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
    # Edge cases
    ((1, []), True),
    ((3, [[1, 0], [2, 1]]), True),
    ((3, [[0, 1], [1, 2], [2, 0]]), False),
    ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), True),
    ((2, []), True),
])
def test_can_finish(args, expected):
    assert Solution().canFinish(*args) == expected
