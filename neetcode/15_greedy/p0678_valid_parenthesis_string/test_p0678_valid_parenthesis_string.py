import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    # LeetCode examples
    (("()",), True),
    (("(*)",), True),
    (("(*))",), True),
    # Edge cases
    (("(",), False),
    ((")",), False),
    (("*",), True),
    (("((*",), False),
    (("**(",), False),
    (("()()",), True),
    (("(*()",), True),
])
def test_check_valid_string(args, expected):
    assert Solution().checkValidString(*args) == expected
