from typing import List, Optional


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def bt(cur, idx):
            if idx == len(nums):
                ans.append(cur[:])
                return

            cur_num = nums[idx]
            cur.append(cur_num)
            bt(cur, idx + 1)
            cur.pop()
            n = 1
            while idx + n < len(nums) and cur_num == nums[idx + n]:
                n += 1
            bt(cur, idx + n)

        bt([], 0)
        return ans
