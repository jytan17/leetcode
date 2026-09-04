from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            if n in hash_map:
                return [i, hash_map[n]]

            hash_map[target - n] = i
