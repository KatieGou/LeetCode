class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_sum=float('-inf')
        sub_sum=0
        for num in nums:
            sub_sum+=num
            max_sum=max(max_sum, sub_sum)
            if sub_sum<0:
                sub_sum=0
        return max_sum
