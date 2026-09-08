import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((4,), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    ((1,), [["Q"]]),
    # Edge cases
    ((2,), []),
    ((3,), []),
    ((5,), 10),
])
def test_solve_n_queens(args, expected):
    result = Solution().solveNQueens(*args)
    if isinstance(expected, int):
        assert len(result) == expected
    else:
        assert sorted(map(tuple, result)) == sorted(map(tuple, expected))
