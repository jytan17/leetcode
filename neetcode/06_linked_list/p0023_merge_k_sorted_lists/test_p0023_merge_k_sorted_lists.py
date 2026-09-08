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


@pytest.mark.parametrize("lists,expected", [
    # LeetCode examples
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
    # Edge cases
    ([[], [1]], [1]),
    ([[1]], [1]),
    ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]),
    ([[-2, -1, 0], [-3, 5], [1, 2]], [-3, -2, -1, 0, 1, 2, 5]),
    ([[], [], []], []),
])
def test_merge_k_lists(lists, expected):
    assert to_list(Solution().mergeKLists([build_list(v) for v in lists])) == expected
