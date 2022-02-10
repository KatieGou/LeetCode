# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def array_to_tree(nums):
            if not nums:
                return
            r, left, right=self.split_tree(nums)
            root=TreeNode(r)
            root.left=array_to_tree(left)
            root.right=array_to_tree(right)
            return root
        
        tree=array_to_tree(nums)
        return tree
        
    def split_tree(self, nums):
        length=len(nums)
        middle_idx=length//2
        r=nums[middle_idx]
        left=nums[:middle_idx]
        right=nums[middle_idx+1:]
        return r, left, right
# recursive method is a must for trees
