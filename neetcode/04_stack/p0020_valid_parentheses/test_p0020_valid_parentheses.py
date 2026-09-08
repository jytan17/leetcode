import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([])",), True),
    # Edge cases
    (("(",), False),
    ((")",), False),
    (("((()))",), True),
    (("{[]}",), True),
    (("([)]",), False),
    (("]{",), False),
])
def test_is_valid(args, expected):
    assert Solution().isValid(*args) == expected
