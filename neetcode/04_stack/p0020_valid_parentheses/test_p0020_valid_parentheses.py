import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([])",), True),
    (("(",), False),
])
def test_is_valid(args, expected):
    assert Solution().isValid(*args) == expected
