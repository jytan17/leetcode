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
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    # Edge cases
    ([1], True),
    ([5, 4, 6, None, None, 3, 7], False),
    ([2, 2, 2], False),
    ([0, None, -1], False),
])
def test_is_valid_bst(vals, expected):
    assert Solution().isValidBST(build_tree(vals)) == expected
