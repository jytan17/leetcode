import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("", ""), True),
    (("a", "ab"), False),
])
def test_is_anagram(args, expected):
    assert Solution().isAnagram(*args) == expected
