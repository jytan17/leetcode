from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def bt(cur, cur_sum, idx):
            if cur_sum == target:
                ans.append(cur[:])
                return

            if idx == len(candidates):
                return

            cur_num = candidates[idx]
            if cur_sum + cur_num <= target:
                cur.append(cur_num)
                bt(cur, cur_sum + cur_num, idx)
                cur.pop()
            bt(cur, cur_sum, idx + 1)

        bt([], 0, 0)
        return ans
