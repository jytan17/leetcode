from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1, split
        slow, fast = head, head
        """
        L1, L2, L3, L4
            ^
                ^
        L1, L2, L3, L4, L5, L6
                ^
                        ^
        """
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        p2 = slow.next
        slow.next = None

        # 2, reverse p2
        prev, cur = None, p2
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        p2 = prev
        p1 = head
        ans = cur = ListNode()
        while True:
            if p1:
                cur.next = p1
                cur = cur.next
                p1 = p1.next

            if p2:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
            else:
                break

        return ans.next
