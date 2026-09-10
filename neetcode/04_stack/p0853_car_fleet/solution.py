from typing import List, Optional


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        p_s = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)

        for p, s in p_s:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)

        print(stack)
        return len(stack)
