# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_list=list()
        for l in lists:
            all_list+=self.convert_to_list(l)
        if not all_list:
            return None
        else:
            all_list.sort()
            return self.convert_to_listnode(all_list)
    
    def convert_to_list(self, l):
        if not l:
            return []
        lst=[l.val]
        while l.next:
            lst.append(l.next.val)
            l=l.next
        return lst
    
    def convert_to_listnode(self, l):
        temp=ListNode(val=l[-1])
        final=temp
        for i in range(len(l)-2, -1, -1):
            temp=ListNode(val=l[i], next=temp)
            final=temp
        return final
