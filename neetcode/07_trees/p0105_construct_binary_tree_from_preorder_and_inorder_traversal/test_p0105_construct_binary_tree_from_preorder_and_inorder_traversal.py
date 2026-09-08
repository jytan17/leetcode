import pytest
from solution import Solution, TreeNode


def to_level_list(root):
    if root is None:
        return []
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


@pytest.mark.parametrize("preorder,inorder,expected", [
    # LeetCode examples
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
    ([-1], [-1], [-1]),
    # Edge cases
    ([1, 2], [2, 1], [1, 2]),
    ([1, 2], [1, 2], [1, None, 2]),
    ([1, 2, 3, 4, 5], [4, 3, 5, 2, 1], [1, 2, None, 3, None, 4, 5]),
])
def test_build_tree(preorder, inorder, expected):
    assert to_level_list(Solution().buildTree(preorder, inorder)) == expected
