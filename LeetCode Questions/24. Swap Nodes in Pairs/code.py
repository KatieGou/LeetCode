# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        output=list()
        while head:
            if head.next:
                head_n_n=head.next.next
                head.next.next=None
                first_node=head
                second_node=head.next
                first_node.next=None
                second_node.next=first_node
                output.append(second_node)
            else:
                output.append(head)
                break
            head=head_n_n
            
        temp=output[-1]
        final=temp
        for i in range(len(output)-2, -1, -1):
            current=output[i]
            current.next.next=temp
            temp=current
            final=temp
        return final
