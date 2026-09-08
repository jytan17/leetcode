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
    # LeetCode examples
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    # Edge cases
    ([5], [1, 2, 3], [1, 2, 3, 5]),
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
    ([1], [2], [1, 2]),
    ([-3, -1, 4], [-2, 0, 5], [-3, -2, -1, 0, 4, 5]),
])
def test_merge_two_lists(a, b, expected):
    assert to_list(Solution().mergeTwoLists(build_list(a), build_list(b))) == expected
