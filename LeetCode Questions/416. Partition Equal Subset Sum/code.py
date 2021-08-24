class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_=sum(nums)
        if sum_%2!=0:
            return 0
        return int(sum_/2) in self.subset_sum(nums)
    
    def subset_sum(self, l):
        s={0}
        for i in l:
            temp={i+j for j in s}
            s.update(temp)
        return s
