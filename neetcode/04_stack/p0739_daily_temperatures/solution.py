from math import inf
from typing import List, Optional


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((t, i))

        return result
