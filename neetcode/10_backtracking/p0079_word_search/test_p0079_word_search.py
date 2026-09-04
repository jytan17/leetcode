import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"), True),
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"), True),
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"), False),
    (([["a"]], "a"), True),
])
def test_exist(args, expected):
    assert Solution().exist(*args) == expected
