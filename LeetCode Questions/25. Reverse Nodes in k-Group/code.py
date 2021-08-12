# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        
        current=head
        prev=None
        reversed_listnode=None
        output=None
        while current:
            processing_node=current
            i=0
            while current and i<k:
                original_next=current.next
                current.next=prev
                prev=current
                current=original_next
                i+=1
            if i<k: # reverse back
                current=prev
                prev=None
                while current:
                    original_next=current.next
                    current.next=prev
                    prev=current
                    current=original_next
            if reversed_listnode is None:
                output=prev
            else:
                # print('output before', output)
                # print('prev', prev)
                # print('rev_ln before', reversed_listnode)
                reversed_listnode.next=prev # attach
                # print('rev_ln after', reversed_listnode)
                # print('output after', output)
            reversed_listnode=processing_node
            prev=None
        return output
