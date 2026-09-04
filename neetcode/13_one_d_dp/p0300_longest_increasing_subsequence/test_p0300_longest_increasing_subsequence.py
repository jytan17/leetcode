import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
    (([0, 1, 0, 3, 2, 3],), 4),
    (([7, 7, 7, 7, 7, 7, 7],), 1),
    (([1],), 1),
])
def test_length_of_l_i_s(args, expected):
    assert Solution().lengthOfLIS(*args) == expected
