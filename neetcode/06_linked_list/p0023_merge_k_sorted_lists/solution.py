import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        lists = [l for l in lists if l]
        heapq.heapify(lists)

        while lists:
            l = heapq.heappop(lists)
            cur.next = l
            cur = cur.next
            l = l.next
            cur.next = None
            if l:
                heapq.heappush(lists, l)

        return dummy.next
