import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("ABAB", 2), 4),
    (("AABABBA", 1), 4),
    (("A", 0), 1),
])
def test_character_replacement(args, expected):
    assert Solution().characterReplacement(*args) == expected
