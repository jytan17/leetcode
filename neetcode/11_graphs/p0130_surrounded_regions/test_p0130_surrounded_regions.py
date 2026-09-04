import pytest
from solution import Solution


@pytest.mark.parametrize("board,expected", [
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
    ([["X"]], [["X"]]),
    ([["O", "O"], ["O", "O"]], [["O", "O"], ["O", "O"]]),
])
def test_solve(board, expected):
    Solution().solve(board)
    assert board == expected
