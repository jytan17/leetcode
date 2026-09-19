from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def bt(start):
            if start == len(nums):
                ans.append(nums[:])
                return

            for idx in range(start, len(nums)):
                nums[start], nums[idx] = nums[idx], nums[start]
                bt(start + 1)
                nums[start], nums[idx] = nums[idx], nums[start]

        bt(0)
        return ans
