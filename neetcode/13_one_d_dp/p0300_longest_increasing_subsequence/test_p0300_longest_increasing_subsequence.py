import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
    (([0, 1, 0, 3, 2, 3],), 4),
    (([7, 7, 7, 7, 7, 7, 7],), 1),
    # Edge cases
    (([1],), 1),
    (([1, 2, 3, 4, 5],), 5),
    (([5, 4, 3, 2, 1],), 1),
    (([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12],), 6),
])
def test_length_of_l_i_s(args, expected):
    assert Solution().lengthOfLIS(*args) == expected
