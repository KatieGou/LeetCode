class Solution:
    def myAtoi(self, s: str) -> int:
        for char in s:
            if char==' ':
                s=s[1:]
            else:
                break
        if len(s)==0:
            return 0
        sign=1
        c=s[0]
        if c=='-':
            sign=-1
            s=s[1:]
        elif c=='+':
            s=s[1:]
        
        for char in s:
            if char=='0':
                s=s[1:]
            else:
                break
        
        res=""
        for char in s:
            if char.isdigit():
                res+=char
            else:
                break
        
        if res=="":
            return 0
        else:
            res=int(res)
            res*=sign
            if res<-2**31:
                return -2**31
            elif res>2**31-1:
                return 2**31-1
            else:
                return res
