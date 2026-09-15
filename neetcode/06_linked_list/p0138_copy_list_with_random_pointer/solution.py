from typing import List, Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional["Node"]) -> Optional["Node"]:
        mapping = {None: None}

        cur = head
        while cur:
            nxt, rnd = cur.next, cur.random
            if cur not in mapping:
                mapping[cur] = Node(cur.val)
            if nxt not in mapping:
                mapping[nxt] = Node(nxt.val)
            if rnd not in mapping:
                mapping[rnd] = Node(rnd.val)

            mapping[cur].next = mapping[nxt]
            mapping[cur].random = mapping[rnd]

            cur = cur.next

        return mapping[head]
