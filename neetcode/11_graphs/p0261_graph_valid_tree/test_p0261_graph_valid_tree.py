import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
    ((5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
    # Edge cases
    ((1, []), True),
    ((2, []), False),
    ((2, [[0, 1]]), True),
    ((4, [[0, 1], [2, 3]]), False),
    ((3, [[0, 1], [1, 2], [0, 2]]), False),
])
def test_valid_tree(args, expected):
    assert Solution().validTree(*args) == expected
