class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        length=len(nums1)+len(nums2)
        if length%2==0:
            return (nums[int(length/2)]+nums[int(length/2)-1])/2
        else:
            return float(nums[int((length-1)/2)])
