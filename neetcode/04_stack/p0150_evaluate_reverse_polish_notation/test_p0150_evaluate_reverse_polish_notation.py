import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    ((["2", "1", "+", "3", "*"],), 9),
    ((["4", "13", "5", "/", "+"],), 6),
    ((["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],), 22),
    # Edge: negative division truncates toward zero
    ((["-7", "2", "/"],), -3),
    # Edge: single number
    ((["18"],), 18),
    # Edge: subtraction
    ((["5", "3", "-"],), 2),
    # Edge: negative result
    ((["3", "5", "-"],), -2),
])
def test_eval_rpn(args, expected):
    assert Solution().evalRPN(*args) == expected
