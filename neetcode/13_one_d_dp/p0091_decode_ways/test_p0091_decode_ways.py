import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("12",), 2),
    (("226",), 3),
    (("06",), 0),
    (("10",), 1),
])
def test_num_decodings(args, expected):
    assert Solution().numDecodings(*args) == expected
