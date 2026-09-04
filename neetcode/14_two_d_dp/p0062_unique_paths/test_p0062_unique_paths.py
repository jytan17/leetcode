import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((3, 7), 28),
    ((3, 2), 3),
    ((1, 1), 1),
    ((1, 10), 1),
])
def test_unique_paths(args, expected):
    assert Solution().uniquePaths(*args) == expected
