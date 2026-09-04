import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((["wrt", "wrf", "er", "ett", "rftt"],), "wertf"),
    ((["z", "x"],), "zx"),
    ((["z", "x", "z"],), ""),
    ((["abc", "ab"],), ""),
])
def test_alien_order(args, expected):
    assert Solution().alienOrder(*args) == expected
