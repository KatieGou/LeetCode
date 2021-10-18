class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        nums.sort()
        # print(nums)
        max_l=0
        cur_l=1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                cur_l+=1
            else:
                cur_l=1
            max_l=max(max_l, cur_l)
        return max_l
