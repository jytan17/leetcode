import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[1, 2, 2, 3, 5],
       [3, 2, 3, 4, 4],
       [2, 4, 5, 3, 1],
       [6, 7, 1, 4, 5],
       [5, 1, 1, 2, 4]],), [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    (([[1]],), [[0, 0]]),
])
def test_pacific_atlantic(args, expected):
    assert sorted(map(tuple, Solution().pacificAtlantic(*args))) == sorted(map(tuple, expected))
