import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([2, 2, 1],), 1),
    (([4, 1, 2, 1, 2],), 4),
    (([1],), 1),
])
def test_single_number(args, expected):
    assert Solution().singleNumber(*args) == expected
