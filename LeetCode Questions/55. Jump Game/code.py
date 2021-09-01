class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        dp=[False]*len(nums)
        dp[0]=True
        max_reach_idx=float('-inf')
        for i in range(len(nums)):
            if dp[i]==True:
                max_reach_idx=max(max_reach_idx, i+nums[i])
                dp[:max_reach_idx+1]=[True]*(max_reach_idx+1)
            if dp[-1]:
                return True
        return False
