# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, l1, l2):
        l = ListNode(0)
        p = l

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1 is not None:
            p.next = l1

        if l2 is not None:
            p.next = l2

        return l.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # step 1. cut the list to two halves
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # step 2. sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.merge(l1, l2)


three = ListNode(3)
one = ListNode(1, three)
two = ListNode(2, one)
four = ListNode(4, two)

solution = Solution()
result = solution.sortList(four)
head = result
while head is not None:
    print(head.val)
    head = head.next
