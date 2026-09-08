import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("aab",), [["a", "a", "b"], ["aa", "b"]]),
    (("a",), [["a"]]),
    # Edge cases
    (("aa",), [["a", "a"], ["aa"]]),
    (("aba",), [["a", "b", "a"], ["aba"]]),
    (("aaa",), [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    (("ab",), [["a", "b"]]),
])
def test_partition(args, expected):
    assert sorted(map(tuple, Solution().partition(*args))) == sorted(map(tuple, expected))
