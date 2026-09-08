import pytest
from solution import Solution, Node


def build(pairs):
    if not pairs:
        return None
    nodes = [Node(val) for val, _ in pairs]
    for i, node in enumerate(nodes):
        node.next = nodes[i + 1] if i + 1 < len(nodes) else None
        idx = pairs[i][1]
        node.random = nodes[idx] if idx is not None else None
    return nodes[0]


def dump(head):
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [(n.val, index.get(id(n.random))) for n in nodes]


@pytest.mark.parametrize("pairs", [
    # LeetCode examples
    [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
    [[1, 1], [2, 1]],
    [[3, None], [3, 0], [3, None]],
    # Edge cases
    [],
    [[1, None]],
    [[1, 0]],
    [[1, 0], [2, 0], [3, 1]],
])
def test_copy_random_list(pairs):
    head = build(pairs)
    copied = Solution().copyRandomList(head)
    if not pairs:
        assert copied is None
        return
    assert dump(copied) == dump(head)
    original = set()
    node = head
    while node:
        original.add(id(node))
        node = node.next
    node = copied
    while node:
        assert id(node) not in original
        node = node.next
