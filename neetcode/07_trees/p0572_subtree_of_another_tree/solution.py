from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if p and q and p.val == q.val:
                return is_same(p.left, q.left) and is_same(p.right, q.right)
            return p is q

        stack = [root]
        while stack:
            cur = stack.pop()
            if is_same(cur, subRoot):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return False
