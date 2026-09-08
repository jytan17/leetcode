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


def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


@pytest.mark.parametrize("vals,p,q,expected", [
    # LeetCode examples
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
    ([2, 1], 2, 1, 2),
    # Edge cases
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5, 4),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0, 5, 2),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 7, 9, 8),
])
def test_lowest_common_ancestor(vals, p, q, expected):
    root = build_tree(vals)
    node = Solution().lowestCommonAncestor(root, find_node(root, p), find_node(root, q))
    assert node.val == expected
