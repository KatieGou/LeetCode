# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        root_lst=[root]
        next_root_lst=list()
        depth=0
        while root_lst:
            depth+=1
            for r in root_lst:
                if r.left: next_root_lst.append(r.left)
                if r.right: next_root_lst.append(r.right)
            root_lst=next_root_lst
            next_root_lst=list()
        return depth
