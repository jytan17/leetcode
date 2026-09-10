import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3),
    ((10, [3], [3]), 1),
    ((100, [0, 2, 4], [4, 2, 1]), 1),
    # Edge: two cars, no merge
    ((10, [0, 5], [1, 3]), 2),
    # Edge: two cars at same speed
    ((10, [2, 4], [3, 3]), 2),
    # Edge: all cars merge into one fleet
    ((10, [6, 8], [3, 2]), 2),
])
def test_car_fleet(args, expected):
    assert Solution().carFleet(*args) == expected
