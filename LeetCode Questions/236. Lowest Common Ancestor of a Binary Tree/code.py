# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents=dict()
        parents[root]=None
        cur_root_lst=[root]
        while (p not in parents) or (q not in parents): # both of them should be in parents
            new_root_lst=list()
            for root in cur_root_lst:
                if root.left:
                    parents[root.left]=root
                    new_root_lst.append(root.left)
                if root.right:
                    parents[root.right]=root
                    new_root_lst.append(root.right)
            cur_root_lst=new_root_lst
        
        # find all ancestor of p
        p_ancestors=[p]
        while p:
            p_ancestors.append(parents[p])
            p=parents[p]
        
        # backtrack q's ancestors
        while q:
            if q in p_ancestors:
                return q
            q=parents[q]
