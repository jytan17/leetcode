from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        level = deque([root]) if root else []
        while level:
            cur_level_len = len(level)
            for i in range(cur_level_len):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                if i == cur_level_len - 1:
                    ans.append(node.val)

        return ans
