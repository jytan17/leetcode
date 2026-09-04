import pytest
from solution import Solution, ListNode


def build_list(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


@pytest.mark.parametrize("a,b,expected", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ([5], [5], [0, 1]),
])
def test_add_two_numbers(a, b, expected):
    assert to_list(Solution().addTwoNumbers(build_list(a), build_list(b))) == expected
