# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) and (not l2):
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        lst1=[l1.val]
        while l1.next is not None:
            lst1.append(l1.next.val)
            l1=l1.next
        
        lst2=[l2.val]
        while l2.next is not None:
            lst2.append(l2.next.val)
            l2=l2.next
        
        lst=lst1+lst2
        lst.sort()
        
        temp=ListNode(val=lst[-1])
        output=temp
        for i in range(len(lst)-2, -1, -1):
            temp=ListNode(val=lst[i], next=temp)
            output=temp
        return output
