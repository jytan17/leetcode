from collections import Counter
from typing import List, Optional


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = Counter()
        ans = 0

        l = 0
        for r in range(len(s)):
            char = s[r]
            hash_map[char] += 1
            while sum(hash_map.values()) - max(hash_map.values()) > k:
                hash_map[s[l]] -= 1
                l += 1
            ans = max(r - l + 1, ans)

        return ans
