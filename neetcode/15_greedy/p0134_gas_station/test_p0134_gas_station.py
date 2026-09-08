import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
    (([2, 3, 4], [3, 4, 3]), -1),
    # Edge cases
    (([5], [4]), 0),
    (([3], [4]), -1),
    (([3, 1, 1], [1, 2, 2]), 0),
    (([0, 0, 0], [0, 0, 0]), 0),
])
def test_can_complete_circuit(args, expected):
    assert Solution().canCompleteCircuit(*args) == expected
