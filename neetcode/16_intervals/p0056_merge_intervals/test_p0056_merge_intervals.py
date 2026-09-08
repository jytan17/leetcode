import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    # Edge cases
    (([[1, 4], [0, 4]],), [[0, 4]]),
    (([[1, 4]],), [[1, 4]]),
    (([[1, 4], [2, 3]],), [[1, 4]]),
    (([[1, 3], [4, 6], [7, 9]],), [[1, 3], [4, 6], [7, 9]]),
    (([[1, 10], [2, 3], [4, 5], [6, 7]],), [[1, 10]]),
])
def test_merge(args, expected):
    assert Solution().merge(*args) == expected
