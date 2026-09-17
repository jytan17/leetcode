from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        level = deque([root]) if root else []
        while level:
            cur_level_vals = []
            for _ in range(len(level)):
                node = level.popleft()
                cur_level_vals.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(cur_level_vals)

        return ans
