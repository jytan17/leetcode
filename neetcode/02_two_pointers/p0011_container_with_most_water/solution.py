from typing import List, Optional


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1

        while l < r:
            water = (r - l) * min(height[r], height[l])
            ans = max(ans, water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans
