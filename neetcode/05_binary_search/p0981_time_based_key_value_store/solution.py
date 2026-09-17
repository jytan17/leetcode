from collections import defaultdict
from typing import List, Optional


class TimeMap:
    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.hash_map[key]
        l, r = 0, len(array)
        ans = ""
        while l < r:
            m = (l + r) // 2
            if array[m][1] <= timestamp:
                ans = array[m][0]
                l = m + 1
            else:
                r = m

        return ans
