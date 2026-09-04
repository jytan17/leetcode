import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((4,), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    ((1,), [["Q"]]),
    ((2,), []),
])
def test_solve_n_queens(args, expected):
    assert sorted(map(tuple, Solution().solveNQueens(*args))) == sorted(map(tuple, expected))
