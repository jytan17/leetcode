import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("rabbbit", "rabbit"), 3),
    (("babgbag", "bag"), 5),
    (("a", "b"), 0),
])
def test_num_distinct(args, expected):
    assert Solution().numDistinct(*args) == expected
