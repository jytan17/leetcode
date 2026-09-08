import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("12",), 2),
    (("226",), 3),
    (("06",), 0),
    # Edge cases
    (("10",), 1),
    (("0",), 0),
    (("1",), 1),
    (("27",), 1),
    (("11106",), 2),
    (("2101",), 1),
    (("1111",), 5),
])
def test_num_decodings(args, expected):
    assert Solution().numDecodings(*args) == expected
