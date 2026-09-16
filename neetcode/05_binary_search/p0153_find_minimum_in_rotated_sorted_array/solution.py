from typing import List, Optional


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                if nums[r] < nums[l]:
                    l = m + 1
                else:
                    return nums[l]
            else:
                r = m
