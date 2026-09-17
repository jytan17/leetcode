from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node, a, b):
            if a.val <= node.val <= b.val:
                return node
            elif b.val < node.val:
                return dfs(node.left, a, b)
            else:
                return dfs(node.right, a, b)

        if p.val > q.val:
            p, q = q, p

        return dfs(root, p, q)
