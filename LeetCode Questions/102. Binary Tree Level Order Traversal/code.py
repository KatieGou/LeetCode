# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # print(root)
        if not root:
            return list()
        if (not root.left) and (not root.right):
            return [[root.val]]
        
        output=[[root.val]]
        root_lst=[root]
        while root_lst:
            # print(root_lst)
            next_root_val_lst=list()
            new_root_lst=list()
            self.traverse(root_lst, next_root_val_lst, new_root_lst)
            if next_root_val_lst:
                output.append(next_root_val_lst)
            root_lst=new_root_lst
        return output
    
    def traverse(self, root_lst, next_root_val_lst, new_root_lst):
        for root in root_lst:
            if root.left:
                next_root_val_lst.append(root.left.val)
                new_root_lst.append(root.left)
            if root.right:
                next_root_val_lst.append(root.right.val)
                new_root_lst.append(root.right)
