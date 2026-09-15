from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()

        while l1 or l2 or carry:
            x = y = 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next

            val = carry + x + y
            cur.next = ListNode(val % 10)
            cur = cur.next
            carry = val >= 10

        return dummy.next
