import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    (("",), []),
    (("2",), ["a", "b", "c"]),
    # Edge cases
    (("7",), ["p", "q", "r", "s"]),
    (("9",), ["w", "x", "y", "z"]),
    (("79",), ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz",
               "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),
])
def test_letter_combinations(args, expected):
    assert sorted(Solution().letterCombinations(*args)) == sorted(expected)
