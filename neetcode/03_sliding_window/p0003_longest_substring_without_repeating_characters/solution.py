from typing import List, Optional


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            cur_char = s[right]
            while cur_char in window:
                window.remove(s[left])
                left += 1
            window.add(cur_char)
            ans = max(ans, len(window))

        return ans
