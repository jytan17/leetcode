import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"), True),
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"), True),
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"), False),
    # Edge cases
    (([["a"]], "a"), True),
    (([["a"]], "b"), False),
    (([["a", "b"], ["c", "d"]], "acdb"), True),
    (([["A", "A"]], "AAA"), False),
])
def test_exist(args, expected):
    assert Solution().exist(*args) == expected
