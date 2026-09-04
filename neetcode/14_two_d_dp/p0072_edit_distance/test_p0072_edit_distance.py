import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("horse", "ros"), 3),
    (("intention", "execution"), 5),
    (("", "a"), 1),
    (("", ""), 0),
])
def test_min_distance(args, expected):
    assert Solution().minDistance(*args) == expected
