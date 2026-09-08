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
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42),
    # Edge cases
    ([-3], -3),
    ([2, -1], 2),
    ([1, -2, -3, 1, 3, -2, None, -1], 3),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
])
def test_max_path_sum(vals, expected):
    assert Solution().maxPathSum(build_tree(vals)) == expected
