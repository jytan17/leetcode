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
    # LeetCode examples
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    # Edge cases
    ([1], 1, [1]),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
    ([1, 2, 3, 4], 2, [2, 1, 4, 3]),
    ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
    ([1, 2], 3, [1, 2]),
])
def test_reverse_k_group(vals, k, expected):
    assert to_list(Solution().reverseKGroup(build_list(vals), k)) == expected
