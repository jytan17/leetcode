import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
    (([1], 1), [1]),
    (([1, -1], 1), [1, -1]),
])
def test_max_sliding_window(args, expected):
    assert Solution().maxSlidingWindow(*args) == expected
