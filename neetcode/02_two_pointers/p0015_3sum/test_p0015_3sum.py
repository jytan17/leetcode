import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    (([0, 1, 1],), []),
    (([0, 0, 0],), [[0, 0, 0]]),
    (([0, 0, 0, 0],), [[0, 0, 0]]),
])
def test_three_sum(args, expected):
    assert sorted(sorted(x) for x in Solution().threeSum(*args)) == sorted(sorted(x) for x in expected)
