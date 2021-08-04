# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l=[head.val]
        while head.next:
            l.append(head.next.val)
            head=head.next
        del l[-n]
        if l:
            temp=ListNode(val=l[-1])
            final=temp
            for i in range(len(l)-2, -1, -1):
                m=ListNode(val=l[i], next=temp)
                temp=m
                final=m
            return final
        else:
            return None
