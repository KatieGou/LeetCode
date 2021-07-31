class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length=len(nums)
        distance=float('inf')
        closest=None
        old=None
        for i in range(length):
            current=nums[i]
            if current!=old:
                j, k=0, length-1
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
                sum_=current+nums[j]+nums[k]
                if sum_==target:
                    return target
                else:
                    dis=abs(sum_-target)
                    if dis<distance:
                        distance=dis
                        closest=sum_
                    if sum_>target:
                        k-=1
                    else:
                        j+=1
        return closest
