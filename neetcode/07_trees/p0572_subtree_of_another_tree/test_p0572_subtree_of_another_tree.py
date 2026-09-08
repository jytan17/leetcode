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


@pytest.mark.parametrize("root,sub,expected", [
    # LeetCode examples
    ([3, 4, 5, 1, 2], [4, 1, 2], True),
    ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    # Edge cases
    ([1], [1], True),
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2, 3], [2], True),
    ([1, 2, 3], [4], False),
])
def test_is_subtree(root, sub, expected):
    assert Solution().isSubtree(build_tree(root), build_tree(sub)) == expected
