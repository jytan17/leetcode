import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
     ["oath", "pea", "eat", "rain"],
     ["oath", "eat"]),
    ([["a", "b"], ["c", "d"]],
     ["abcb"],
     []),
    # Single cell
    ([["a"]],
     ["a"],
     ["a"]),
    # No words found
    ([["a", "b"], ["c", "d"]],
     ["xyz"],
     []),
    # Word uses entire board path
    ([["a", "b"], ["d", "c"]],
     ["abcd", "abdc"],
     ["abcd"]),
])
def test_find_words(args, expected):
    board, words, exp = args[0], args[1], expected
    assert sorted(Solution().findWords(board, words)) == sorted(exp)
