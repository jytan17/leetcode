from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m

            return l < len(nums) and nums[l] == target

        top, bot = 0, len(matrix) - 1

        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return binary_search(matrix[m], target)
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                top = m + 1

        return False
