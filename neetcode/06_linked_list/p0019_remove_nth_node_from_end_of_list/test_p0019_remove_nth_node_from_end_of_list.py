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


@pytest.mark.parametrize("vals,n,expected", [
    # LeetCode examples
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    # Edge cases
    ([1, 2], 2, [2]),
    ([1, 2, 3], 3, [2, 3]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
])
def test_remove_nth_from_end(vals, n, expected):
    assert to_list(Solution().removeNthFromEnd(build_list(vals), n)) == expected
