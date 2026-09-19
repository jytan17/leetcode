from typing import List, Optional


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def bt(cur_arr, cur_sum, idx):
            if cur_sum == target:
                ans.append(cur_arr[:])
                return

            if idx == len(candidates):
                return

            cur_num = candidates[idx]
            if cur_sum + cur_num <= target:
                cur_arr.append(cur_num)
                bt(cur_arr, cur_sum + cur_num, idx + 1)
                cur_arr.pop()

            n = 1
            while idx + n < len(candidates) and cur_num == candidates[idx + n]:
                n += 1
            bt(cur_arr, cur_sum, idx + n)

        bt([], 0, 0)
        return ans
