from typing import List, Optional


class MinStack:
    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        if self.array:
            _, cur_min = self.array[-1]
        else:
            cur_min = val

        self.array.append((val, min(val, cur_min)))

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return self.array[-1][0]

    def getMin(self) -> int:
        return self.array[-1][1]
