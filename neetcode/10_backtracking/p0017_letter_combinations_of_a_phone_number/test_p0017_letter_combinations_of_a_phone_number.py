import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    (("",), []),
    (("2",), ["a", "b", "c"]),
])
def test_letter_combinations(args, expected):
    assert sorted(Solution().letterCombinations(*args)) == sorted(expected)
