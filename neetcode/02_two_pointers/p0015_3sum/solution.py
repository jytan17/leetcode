from typing import List, Optional


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        i = 0

        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            x = nums[i]
            while j < k:
                y, z = nums[j], nums[k]
                S = x + y + z
                if S == 0:
                    out.append([x, y, z])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                elif S <= 0:
                    j += 1
                else:
                    k -= 1

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return out
