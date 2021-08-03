class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length=len(nums)
        res=list()
        old_i=None
        for i in range(length):
            current_i=nums[i]
            if current_i!=old_i:
                old_i=current_i
                old_j=None
                for j in range(i+1, length):
                    current_j=nums[j]
                    if current_j!=old_j:
                        old_j=current_j
                        m, n=0, length-1
                        t=target-(current_i+current_j)
                    else:
                        continue
                    while m<n:
                        if m==i or m==j:
                            m+=1
                            continue
                        if n==i or n==j:
                            n-=1
                            continue
                        if nums[m]+nums[n]==t:
                            l=[current_i, current_j, nums[m], nums[n]]
                            l.sort()
                            if l not in res:
                                res.append(l)
                            m+=1
                            n-=1
                        elif nums[m]+nums[n]<t:
                            m+=1
                        else:
                            n-=1
            else:
                continue
        return res
