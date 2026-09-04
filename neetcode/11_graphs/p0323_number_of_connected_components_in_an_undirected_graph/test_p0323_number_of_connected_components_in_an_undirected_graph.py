import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((5, [[0, 1], [1, 2], [3, 4]]), 2),
    ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
    ((3, []), 3),
])
def test_count_components(args, expected):
    assert Solution().countComponents(*args) == expected
