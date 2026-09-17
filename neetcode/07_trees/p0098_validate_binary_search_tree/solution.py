from math import inf
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_so_far, max_so_far):
            if not node:
                return True

            if not min_so_far < node.val < max_so_far:
                return False
            return helper(node.left, min_so_far, node.val) and helper(
                node.right, node.val, max_so_far
            )

        return helper(root, -inf, inf)
