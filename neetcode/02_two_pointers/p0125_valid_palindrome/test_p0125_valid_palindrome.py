import pytest
from solution import Solution


@pytest.mark.parametrize("args,expected", [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    ((" ",), True),
    (("0P",), False),
])
def test_is_palindrome(args, expected):
    assert Solution().isPalindrome(*args) == expected
