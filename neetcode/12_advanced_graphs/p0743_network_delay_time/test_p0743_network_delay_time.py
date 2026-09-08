import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
    (([[1, 2, 1]], 2, 1), 1),
    (([[1, 2, 1]], 2, 2), -1),
    # Edge cases
    (([], 1, 1), 0),
    (([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1), 3),
    (([[1, 2, 1], [2, 1, 1]], 2, 1), 1),
])
def test_network_delay_time(args, expected):
    assert Solution().networkDelayTime(*args) == expected
