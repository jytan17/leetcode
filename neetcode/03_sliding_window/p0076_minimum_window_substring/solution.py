from collections import Counter
from typing import List, Optional


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(current, target):
            for k, v in target.items():
                if current[k] < v:
                    return False
            return True

        target = Counter(t)

        current = Counter()
        ans = None
        left = 0
        for right in range(len(s)):
            char = s[right]
            current[char] += 1

            while is_valid(current, target):
                new_candidate = s[left : right + 1]
                if ans is None or len(new_candidate) < len(ans):
                    ans = new_candidate
                current[s[left]] -= 1
                left += 1

        return ans if ans else ""
