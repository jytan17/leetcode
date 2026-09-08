import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("leetcode", ["leet", "code"]), True),
    (("applepenapple", ["apple", "pen"]), True),
    (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
    # Edge cases
    (("a", ["a"]), True),
    (("ab", ["a", "b"]), True),
    (("ab", ["a"]), False),
    (("aaaaaaa", ["aaa", "aaaa"]), True),
    (("cars", ["car", "ca", "rs"]), True),
])
def test_word_break(args, expected):
    assert Solution().wordBreak(*args) == expected
