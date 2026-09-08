import pytest
from solution import Solution, ListNode


def build_list(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def build_cycle(vals, pos):
    head = build_list(vals)
    if head is None:
        return None
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return head


@pytest.mark.parametrize("vals,pos,expected", [
    # LeetCode examples
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False),
    # Edge cases
    ([], -1, False),
    ([1, 2, 3], -1, False),
    ([1, 2, 3, 4], 3, True),
    ([1], 0, True),
    ([1, 2, 3, 4, 5], 2, True),
])
def test_has_cycle(vals, pos, expected):
    assert Solution().hasCycle(build_cycle(vals, pos)) == expected
