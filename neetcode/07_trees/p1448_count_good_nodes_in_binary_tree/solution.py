from math import inf
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(node, max_val):
            if not node:
                return

            if node.val >= max_val:
                self.ans += 1
            helper(node.left, max(node.val, max_val))
            helper(node.right, max(node.val, max_val))

        helper(root, -inf)
        return self.ans
