# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        print(root)
        if not root:
            return None
        output=list()
        self.traverse(root, output)
        return output
    
    def traverse(self, root, output):
        if root:
            if root.left:
                self.traverse(root.left, output)
            output.append(root.val)
            if root.right:
                self.traverse(root.right, output)
        else:
            return
