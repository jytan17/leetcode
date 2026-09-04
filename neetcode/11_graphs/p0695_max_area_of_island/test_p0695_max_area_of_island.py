import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],), 6),
    (([[0, 0, 0, 0, 0, 0, 0, 0]],), 0),
    (([[1, 1], [1, 0]],), 3),
])
def test_max_area_of_island(args, expected):
    assert Solution().maxAreaOfIsland(*args) == expected
