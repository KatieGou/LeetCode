# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: BFS, check each node in two lists
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_lst=[p]
        q_lst=[q]
        while len(p_lst)==len(q_lst):
            if not p_lst:
                return True
            p_new_lst=list()
            q_new_lst=list()
            for i in range(len(p_lst)):
                # print('i=', i)
                # print(p_lst)
                # print(q_lst)
                if p_lst[i] and q_lst[i]:
                    if p_lst[i].val!=q_lst[i].val:
                        return False
                    p_new_lst.append(p_lst[i].left)
                    p_new_lst.append(p_lst[i].right)
                    q_new_lst.append(q_lst[i].left)
                    q_new_lst.append(q_lst[i].right)
                elif not (p_lst[i] or q_lst[i]):
                    pass
                else:
                    return False
            p_lst=p_new_lst
            q_lst=q_new_lst
        return False

# Solution 2: Recursive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
