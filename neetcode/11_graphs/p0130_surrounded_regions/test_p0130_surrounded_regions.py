import pytest
from solution import Solution


@pytest.mark.parametrize("board,expected", [
    # LeetCode examples
    ([["X", "X", "X", "X"],
      ["X", "O", "O", "X"],
      ["X", "X", "O", "X"],
      ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "O", "X", "X"]]),
    ([["X"]], [["X"]]),
    # Edge cases
    ([["O"]], [["O"]]),
    ([["O", "O"], ["O", "O"]], [["O", "O"], ["O", "O"]]),
    ([["X", "O", "X"],
      ["O", "X", "O"],
      ["X", "O", "X"]],
     [["X", "O", "X"],
      ["O", "X", "O"],
      ["X", "O", "X"]]),
    ([["X", "X", "X"],
      ["X", "O", "X"],
      ["X", "X", "X"]],
     [["X", "X", "X"],
      ["X", "X", "X"],
      ["X", "X", "X"]]),
])
def test_solve(board, expected):
    Solution().solve(board)
    assert board == expected
