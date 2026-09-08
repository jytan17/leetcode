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
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    ([1, None, 3], [1, 3]),
    ([], []),
    # Edge cases
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3, 4], [1, 3, 4]),
])
def test_right_side_view(vals, expected):
    assert Solution().rightSideView(build_tree(vals)) == expected
