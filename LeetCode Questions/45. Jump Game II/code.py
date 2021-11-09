class Solution:
    def jump(self, nums: List[int]) -> int:
        length=len(nums)
        if length<=1:
            return 0
        step=0
        max_pos=0
        last_pos=0
        for i in range(length):
            max_pos=max(max_pos, i+nums[i])
            if max_pos>=length-1:
                return step+1
            if last_pos==i:
                step+=1
                last_pos=max_pos
        return step
