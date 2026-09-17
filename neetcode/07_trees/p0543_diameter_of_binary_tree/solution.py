from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def helper(node):
            if not node:
                return 0

            left, right = helper(node.left), helper(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        helper(root)

        return self.ans
