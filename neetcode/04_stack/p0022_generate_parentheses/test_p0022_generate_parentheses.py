import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((3,), ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ((1,), ["()"]),
    # Edge / extra
    ((2,), ["(())", "()()"]),
    ((4,), [
        "(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
        "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
        "()(()())", "()(())()", "()()(())", "()()()()",
    ]),
])
def test_generate_parenthesis(args, expected):
    assert sorted(Solution().generateParenthesis(*args)) == sorted(expected)
