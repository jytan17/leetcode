from typing import List, Optional


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def bt(cur, left, right):
            if left == right == n:
                result.append("".join(cur))

            if n > left:
                cur.append("(")
                bt(cur, left + 1, right)
                cur.pop()
            if right < left:
                cur.append(")")
                bt(cur, left, right + 1)
                cur.pop()

        bt([], 0, 0)
        return result
