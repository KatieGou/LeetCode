# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        cur=head
        while cur.next:
            # print('cur:', cur)
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
            # print('head:', head)
        return head
