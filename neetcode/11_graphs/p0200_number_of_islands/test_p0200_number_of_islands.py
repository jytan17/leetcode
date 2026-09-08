import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]], 1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]], 3),
    # Edge cases
    ([["0"]], 0),
    ([["1"]], 1),
    ([["1", "0", "1", "0", "1"]], 3),
    ([["1", "1", "1"],
      ["0", "1", "0"],
      ["1", "1", "1"]], 1),
    ([["0", "0", "0"],
      ["0", "0", "0"]], 0),
])
def test_num_islands(args, expected):
    assert Solution().numIslands(args) == expected
