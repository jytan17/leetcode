from collections import Counter
from typing import List, Optional


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in nums]

        for key, val in Counter(nums).items():
            buckets[val - 1].append(key)

        out = []
        while len(out) < k:
            out.extend(buckets.pop())

        return out
