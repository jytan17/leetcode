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


@pytest.mark.parametrize("vals,expected", [
    # LeetCode examples
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    # Edge cases
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
])
def test_reorder_list(vals, expected):
    head = build_list(vals)
    Solution().reorderList(head)
    assert to_list(head) == expected
