import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("leetcode", ["leet", "code"]), True),
    (("applepenapple", ["apple", "pen"]), True),
    (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
])
def test_word_break(args, expected):
    assert Solution().wordBreak(*args) == expected
