class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
            x=-x
        s=str(x)
        s=s[::-1]
        res=int(s)*sign
        if res<-2147483648 or res>2147483647:
            return 0
        return res
