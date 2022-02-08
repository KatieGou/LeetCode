class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=list()
        for i in range(1, numRows+1):
            res.append([1]*i)
        
        if numRows<=2:
            return res
        
        for i in range(2, numRows):
            prev=res[i-1]
            cur=res[i]
            l=len(cur)
            for j in range(1, l-1):
                cur[j]=prev[j-1]+prev[j]
        
        return res
# 利用python给数据挂标签的设定
