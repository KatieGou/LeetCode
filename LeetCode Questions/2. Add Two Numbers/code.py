# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_lst=[l1.val]
        while l1.next is not None:
            l1_lst.append(l1.next.val)
            l1=l1.next
        len_1=len(l1_lst)
        
        l2_lst=[l2.val]
        while l2.next is not None:
            l2_lst.append(l2.next.val)
            l2=l2.next
        len_2=len(l2_lst)
        
        l1_lst.reverse()
        l2_lst.reverse()
        
        reverse_1=0
        for num in l1_lst:
            reverse_1+=num*(10**(len_1-1))
            len_1-=1
        
        reverse_2=0
        for num in l2_lst:
            reverse_2+=num*(10**(len_2-1))
            len_2-=1
        
        result=str(reverse_1+reverse_2)
        result_lst=[]
        for i in range(len(result)):
            result_lst.append(int(result[i]))
        result_lst.reverse()
        
        temp=ListNode(val=result_lst[-1])
        final=temp
        for i in range(len(result_lst)-2, -1, -1):
            m=ListNode(val=result_lst[i], next=temp)
            temp=m
            final=m
        return final
