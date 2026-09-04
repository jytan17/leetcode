import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[1, 2], [1, 3], [2, 3]],), [2, 3]),
    (([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],), [1, 4]),
])
def test_find_redundant_connection(args, expected):
    assert Solution().findRedundantConnection(*args) == expected
