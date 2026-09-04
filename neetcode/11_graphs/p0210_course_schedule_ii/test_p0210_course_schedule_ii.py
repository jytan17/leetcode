import pytest
from solution import Solution


def is_valid_order(order, n, prereqs):
    if sorted(order) != list(range(n)):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[b] < pos[a] for a, b in prereqs)


@pytest.mark.parametrize("n,prereqs", [
    (2, [[1, 0]]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (1, []),
])
def test_find_order_valid(n, prereqs):
    assert is_valid_order(Solution().findOrder(n, prereqs), n, prereqs)


def test_find_order_cycle():
    assert Solution().findOrder(2, [[1, 0], [0, 1]]) == []
