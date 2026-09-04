import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((3,), ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ((1,), ["()"]),
    ((2,), ["(())", "()()"]),
])
def test_generate_parenthesis(args, expected):
    assert sorted(Solution().generateParenthesis(*args)) == sorted(expected)
