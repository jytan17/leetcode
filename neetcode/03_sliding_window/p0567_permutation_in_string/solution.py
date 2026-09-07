from collections import Counter
from typing import List, Optional


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter()
        for char in s1:
            window[char] += 1

        l = 0
        for char in s2:
            window[char] -= 1
            while min(window.values()) < 0:
                window[s2[l]] += 1
                l += 1

            if min(window.values()) == max(window.values()) == 0:
                return True

        return False
