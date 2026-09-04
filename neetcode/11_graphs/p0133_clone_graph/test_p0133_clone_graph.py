import pytest
from solution import Solution, Node


def build(adj):
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0] if nodes else None


def dump(node):
    if node is None:
        return []
    seen = {}
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur.val in seen:
            continue
        seen[cur.val] = sorted(n.val for n in cur.neighbors)
        stack.extend(cur.neighbors)
    return [seen[k] for k in sorted(seen)]


def collect_ids(node):
    if node is None:
        return set()
    seen = {}
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur.val in seen:
            continue
        seen[cur.val] = id(cur)
        stack.extend(cur.neighbors)
    return set(seen.values())


@pytest.mark.parametrize("adj", [
    [[2, 4], [1, 3], [2, 4], [1, 3]],
    [[]],
    [],
])
def test_clone_graph(adj):
    original = build(adj)
    copied = Solution().cloneGraph(original)
    assert dump(copied) == dump(original)
    assert collect_ids(copied).isdisjoint(collect_ids(original))
