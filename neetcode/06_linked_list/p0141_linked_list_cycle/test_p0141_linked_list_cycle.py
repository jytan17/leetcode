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
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False),
    ([], -1, False),
    ([1, 2, 3], -1, False),
])
def test_has_cycle(vals, pos, expected):
    assert Solution().hasCycle(build_cycle(vals, pos)) == expected
