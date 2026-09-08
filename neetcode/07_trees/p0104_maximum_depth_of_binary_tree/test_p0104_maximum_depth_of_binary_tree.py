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


@pytest.mark.parametrize("vals,expected", [
    # LeetCode examples
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    # Edge cases
    ([], 0),
    ([1], 1),
    ([1, 2, 3, 4], 3),
    ([1, None, 2, None, 3, None, 4], 4),
])
def test_max_depth(vals, expected):
    assert Solution().maxDepth(build_tree(vals)) == expected
