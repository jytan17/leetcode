import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("aab",), [["a", "a", "b"], ["aa", "b"]]),
    (("a",), [["a"]]),
    (("aa",), [["a", "a"], ["aa"]]),
])
def test_partition(args, expected):
    assert sorted(map(tuple, Solution().partition(*args))) == sorted(map(tuple, expected))
