import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((["A", "A", "A", "B", "B", "B"], 2), 8),
    ((["A", "C", "A", "B", "D", "B"], 1), 6),
    ((["A", "A", "A", "B", "B", "B"], 3), 10),
    ((["A"], 0), 1),
])
def test_least_interval(args, expected):
    assert Solution().leastInterval(*args) == expected
