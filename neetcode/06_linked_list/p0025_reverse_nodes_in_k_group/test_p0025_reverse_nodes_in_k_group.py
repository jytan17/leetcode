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


@pytest.mark.parametrize("vals,k,expected", [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1], 1, [1]),
    ([1, 2, 3], 1, [1, 2, 3]),
])
def test_reverse_k_group(vals, k, expected):
    assert to_list(Solution().reverseKGroup(build_list(vals), k)) == expected
