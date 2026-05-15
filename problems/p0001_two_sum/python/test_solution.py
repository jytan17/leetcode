import pytest
from solution import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1000000000, -1000000000], 0, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    got = Solution().twoSum(nums, target)
    assert sorted(got) == sorted(expected)
