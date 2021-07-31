class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        nums.sort()
        length=len(nums)
        res=list()
        old=None
        for i in range(length):
            current=nums[i]
            if current!=old:
                j, k=0, length-1
                target=-current
                old=current
            else:
                continue
            while j<k:
                if j==i:
                    j+=1
                    continue
                if k==i:
                    k-=1
                    continue
                if nums[j]+nums[k]==target:
                    l=[current, nums[j], nums[k]]
                    l.sort()
                    if l not in res:
                        res.append(l)
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1
        return res
