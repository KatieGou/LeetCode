class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr, subset, res):
            res.append(subset)
            print(arr, subset, res)
            print()
            for i in range(len(arr)):
                print('arr=', arr, 'i=', i, 'arr[i]=', arr[i])
                dfs(arr[i+1:], subset+[arr[i]], res)
        res=list()
        dfs(nums, [], res)
        return res
