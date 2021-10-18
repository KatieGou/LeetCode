# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, limits):
            v1, v2=True, True
            if not root:
                return True
            if root.val<=limits[0] or root.val>=limits[1]:
                return False
            if root.left:
                l_limit=[limits[0], min(limits[1], root.val)]
                v1=validate(root.left, l_limit)
            if root.right:
                r_limit=[max(limits[0], root.val), limits[1]]
                v2=validate(root.right, r_limit)
            return v1 and v2
        return validate(root, [-2**31-1, 2**31])
