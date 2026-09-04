import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([[1, 3], [-2, 2]], 1), [[-2, 2]]),
    (([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]]),
    (([[0, 1]], 1), [[0, 1]]),
])
def test_k_closest(args, expected):
    assert sorted(map(tuple, Solution().kClosest(*args))) == sorted(map(tuple, expected))
