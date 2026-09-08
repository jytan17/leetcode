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
    ([3, 1, 4, 3, None, 1, 5], 4),
    ([3, 3, None, 4, 2], 3),
    ([1], 1),
    # Edge cases
    ([2, 2, 2], 3),
    ([9, 3, 6], 1),
    ([1, 2, 3, 4, 5], 5),
])
def test_good_nodes(vals, expected):
    assert Solution().goodNodes(build_tree(vals)) == expected
