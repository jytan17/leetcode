import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    ((["2", "1", "+", "3", "*"],), 9),
    ((["4", "13", "5", "/", "+"],), 6),
    ((["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],), 22),
    ((["-7", "2", "/"],), -3),
])
def test_eval_r_p_n(args, expected):
    assert Solution().evalRPN(*args) == expected
