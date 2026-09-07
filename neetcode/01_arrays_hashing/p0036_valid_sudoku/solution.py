from typing import List, Optional


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            x = set()
            y = set()
            for c in range(9):
                cur_x = board[r][c]
                cur_y = board[c][r]

                if cur_x in x or cur_y in y:
                    return False
                if cur_x != ".":
                    x.add(cur_x)
                if cur_y != ".":
                    y.add(cur_y)

                if r % 3 == 0 and c % 3 == 0:
                    box = set()
                    for i in range(3):
                        for j in range(3):
                            v = board[r + i][c + j]
                            if v in box:
                                return False
                            if v != ".":
                                box.add(v)

        return True
