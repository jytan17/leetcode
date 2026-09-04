import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("()",), True),
    (("(*)",), True),
    (("(*))",), True),
    ((")(",), False),
    (("",), True),
])
def test_check_valid_string(args, expected):
    assert Solution().checkValidString(*args) == expected
