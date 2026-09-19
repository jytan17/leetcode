from typing import List, Optional


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def bt(cur, idx):
            if idx == len(nums):
                self.ans.append(cur.copy())
                return

            cur.append(nums[idx])
            bt(cur, idx + 1)
            cur.pop()
            bt(cur, idx + 1)

        bt([], 0)

        return self.ans
