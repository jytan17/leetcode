import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
       ["oath", "pea", "eat", "rain"]), ["oath", "eat"]),
    (([["a", "b"], ["c", "d"]], ["abcb"]), []),
    (([["a"]], ["a"]), ["a"]),
])
def test_find_words(args, expected):
    assert sorted(Solution().findWords(*args)) == sorted(expected)
