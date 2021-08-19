class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1]<nums[i]:
                # print(i)
                larger_num=1000
                for j in range(i, len(nums)):
                    if nums[j]>nums[i-1] and nums[j]<larger_num:
                        # print(nums[j])
                        temp=nums[j]
                        larger_num=temp
                        idx=j
                # print(j)
                nums[idx]=nums[i-1]
                nums[i-1]=temp
                nums[i:]=sorted(nums[i:])
                break
        else:
            nums.reverse()
