import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("rabbbit", "rabbit"), 3),
    (("babgbag", "bag"), 5),
    # Edge cases
    (("a", "b"), 0),
    (("a", "a"), 1),
    (("aaa", "a"), 3),
    (("", "a"), 0),
    (("abc", ""), 1),
    (("aabb", "ab"), 4),
])
def test_num_distinct(args, expected):
    assert Solution().numDistinct(*args) == expected
