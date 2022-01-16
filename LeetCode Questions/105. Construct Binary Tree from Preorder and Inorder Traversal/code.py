# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            if left>right:
                return None
            
            nonlocal preorder_idx

            root_val=preorder[preorder_idx]
            root=TreeNode(root_val)
            preorder_idx+=1
            
            inorder_idx=dic[root_val]
            root.left=array_to_tree(left, inorder_idx-1)
            root.right=array_to_tree(inorder_idx+1, right)
            
            return root
        
        preorder_idx=0
        dic=dict()
        for i in range(len(inorder)):
            dic[inorder[i]]=i # value: idx

        tree=array_to_tree(0, len(inorder)-1)
        return tree
