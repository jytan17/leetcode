import pytest
from solution import Solution


def is_valid_order(order, n, prereqs):
    if sorted(order) != list(range(n)):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[b] < pos[a] for a, b in prereqs)


@pytest.mark.parametrize("n,prereqs", [
    # LeetCode examples
    (2, [[1, 0]]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (1, []),
    # Edge cases
    (3, [[1, 0], [2, 1]]),
    (2, []),
    (5, [[1, 0], [2, 0], [3, 1], [4, 2]]),
])
def test_find_order_valid(n, prereqs):
    result = Solution().findOrder(n, prereqs)
    assert is_valid_order(result, n, prereqs)


@pytest.mark.parametrize("n,prereqs", [
    (2, [[1, 0], [0, 1]]),
    (3, [[0, 1], [1, 2], [2, 0]]),
])
def test_find_order_cycle(n, prereqs):
    assert Solution().findOrder(n, prereqs) == []
