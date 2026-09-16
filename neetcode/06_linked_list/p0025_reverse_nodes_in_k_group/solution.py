from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def helper(h):
            prev, cur = None, h

            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev, h

        dummy = cur = ListNode()
        dummy.next = head
        slow = fast = cur

        while fast:
            for _ in range(k):
                fast = fast.next
                if not fast:
                    break
            else:
                next_head = fast.next
                fast.next = None
                cur_head = slow.next

                rev_head, rev_tail = helper(cur_head)

                slow.next = rev_head
                rev_tail.next = next_head
                slow = fast = rev_tail

        return dummy.next
