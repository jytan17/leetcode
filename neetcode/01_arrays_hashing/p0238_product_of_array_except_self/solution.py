from typing import List, Optional


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        right = [1 for _ in range(N)]
        left = [1 for _ in range(N)]

        x = 1
        """
        it1. [1, 1, 1, 1] x = 1
                 ^
        it2. [1, 1, 2, 1] x = 1
                    ^
        it3. [1, 1, 2, 6] x = 2
                       ^

        it1. [1, 1, 4, 1] x = 1
                    ^

        it2. [1, 12, 4, 1] x = 4
                 ^

        it2. [24, 12, 4, 1] x = 12
              ^

        it1. [1, 1, 1, 1, 1] x = 1
        it2. [1, -1, -1, 1, 1] x = -1
        it3. [1, -1, -1, 0, 1] x = 0
        it4. [1, -1, -1, 0, 0] x = 0
        """
        for i in range(1, N):
            x *= nums[i - 1]
            right[i] = x

        x = 1
        for i in range(N - 2, -1, -1):
            x *= nums[i + 1]
            left[i] = x

        out = []
        for i in range(N):
            out.append(right[i] * left[i])

        return out
