import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((5, [[0, 1], [1, 2], [3, 4]]), 2),
    ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
    # Edge cases
    ((1, []), 1),
    ((3, []), 3),
    ((4, [[0, 1], [2, 3]]), 2),
    ((6, [[0, 1], [1, 2], [3, 4], [4, 5]]), 2),
])
def test_count_components(args, expected):
    assert Solution().countComponents(*args) == expected
