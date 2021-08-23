class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]
        output=list()
        i=0
        j=len(nums)-1
        while i<=j:
#             print(i, j)
            m=(i+j)//2
#             print(i, j, m)
            if nums[m]==target:
                temp=m
                while temp>=0 and nums[temp]==target:
                    temp-=1
                output.append(temp+1)
                temp=m
                while temp<=len(nums)-1 and nums[temp]==target:
                    temp+=1
                output.append(temp-1)
                return output
            elif nums[m]>target:
                j=m-1
            else:
                i=m+1
