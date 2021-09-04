class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums=sorted(nums, reverse=True, key=str)
        changed=True
        while changed:
            changed=False
            for i in range(1, len(nums)):
                if self.check_whether_swap(nums[i-1], nums[i]):
                    nums[i-1], nums[i]=nums[i], nums[i-1]
                    changed=True
        return str(int(''.join(nums)))
     
    def check_whether_swap(self, s1, s2):
        if s2 in s1:
            if int(s2+s1)>int(s1+s2):
                return True
        return False
