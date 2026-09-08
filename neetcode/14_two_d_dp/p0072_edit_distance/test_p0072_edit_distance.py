import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("horse", "ros"), 3),
    (("intention", "execution"), 5),
    # Edge cases
    (("", ""), 0),
    (("", "a"), 1),
    (("a", ""), 1),
    (("abc", "abc"), 0),
    (("a", "b"), 1),
    (("sea", "eat"), 3),
])
def test_min_distance(args, expected):
    assert Solution().minDistance(*args) == expected
