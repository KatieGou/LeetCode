class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=list()
        intervals.sort()
        for i in intervals:
            if not res:
                res.append(i)
            elif res[-1][1]<i[0]: # no overlap
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1], i[1])
        return res

    def overlap(self, l1, l2):
        if l1[1]>=l2[0] and l1[0]<=l2[1]:
            return True
        return False
