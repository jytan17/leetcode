import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([3, 0, 1],), 2),
    (([0, 1],), 2),
    (([9, 6, 4, 2, 3, 5, 7, 0, 1],), 8),
    (([0],), 1),
])
def test_missing_number(args, expected):
    assert Solution().missingNumber(*args) == expected
