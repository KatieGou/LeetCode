# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast=head
        slow=head
        while (fast is not None) and (fast.next is not None):
            fast=fast.next.next
            if fast is None:
                return False
            slow=slow.next
            if fast==slow:
                return True
        return False
