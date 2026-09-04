import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 3],), [1, 2, 4]),
    (([4, 3, 2, 1],), [4, 3, 2, 2]),
    (([9],), [1, 0]),
    (([9, 9],), [1, 0, 0]),
])
def test_plus_one(args, expected):
    assert Solution().plusOne(*args) == expected
