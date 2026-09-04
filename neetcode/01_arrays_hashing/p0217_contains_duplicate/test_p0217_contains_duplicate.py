import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3, 4],), False),
    (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True),
    (([1],), False),
])
def test_contains_duplicate(args, expected):
    assert Solution().containsDuplicate(*args) == expected
