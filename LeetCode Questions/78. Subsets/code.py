class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr, subset, res):
            res.append(subset)
            for i in range(len(arr)):
                dfs(arr[i+1:], subset+[arr[i]], res)
        res=list()
        dfs(nums, [], res)
        return res
