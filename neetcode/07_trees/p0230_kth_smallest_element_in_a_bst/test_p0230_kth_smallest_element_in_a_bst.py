import pytest
from solution import Solution, TreeNode


def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


@pytest.mark.parametrize("vals,k,expected", [
    # LeetCode examples
    ([3, 1, 4, None, 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    # Edge cases
    ([1], 1, 1),
    ([3, 1, 4, None, 2], 4, 4),
    ([5, 3, 6, 2, 4, None, None, 1], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 6, 6),
])
def test_kth_smallest(vals, k, expected):
    assert Solution().kthSmallest(build_tree(vals), k) == expected
