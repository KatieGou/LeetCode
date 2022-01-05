# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l_tree, r_tree=root.left, root.right
        return self.check_two_trees(l_tree, r_tree)
    
    def check_two_trees(self, l_tree, r_tree):
        print(l_tree)
        print(r_tree)
        print()
        if l_tree:
            if not r_tree:
                return False
            else:
                if l_tree.val==r_tree.val:
                    flag=True
                else:
                    return False
        else:
            if r_tree:
                return False
            else:
                return True
        return flag and self.check_two_trees(l_tree.left, r_tree.right) and self.check_two_trees(l_tree.right, r_tree.left)
