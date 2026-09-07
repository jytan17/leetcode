from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            ans = max(prices[i] - min_price, ans)
            min_price = min(min_price, prices[i])

        return ans
