import math
from typing import List, Optional


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            n = 0
            for p in piles:
                n += math.ceil(p / k)
            return n <= h

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            k = (l + r) // 2
            if can_finish(k):
                r = k - 1
                ans = k
            else:
                l = k + 1

        return ans
