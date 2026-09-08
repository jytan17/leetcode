import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
    (([30, 40, 50, 60],), [1, 1, 1, 0]),
    (([30, 60, 90],), [1, 1, 0]),
    # Edge: single element
    (([50],), [0]),
    # Edge: all same temperature
    (([70, 70, 70, 70],), [0, 0, 0, 0]),
    # Edge: strictly decreasing
    (([90, 80, 70, 60],), [0, 0, 0, 0]),
])
def test_daily_temperatures(args, expected):
    assert Solution().dailyTemperatures(*args) == expected
