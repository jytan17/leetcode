from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in height]
        right = [0 for _ in height]

        cur_max = 0
        for i in range(len(height)):
            left[i] = cur_max
            cur_max = max(height[i], cur_max)

        cur_max = 0
        for j in range(len(height) - 1, -1, -1):
            right[j] = cur_max
            cur_max = max(height[j], cur_max)

        water = []
        for i in range(len(height)):
            water.append(max(0, min(left[i], right[i]) - height[i]))

        return sum(water)
