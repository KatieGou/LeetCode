class Solution:
    def romanToInt(self, s: str) -> int:
        length=len(s)
        res=0
        for i in range(length):
            c=s[i]
            if c=='I':
                res+=1
            elif c=='V':
                res+=5
            elif c=='X':
                res+=10
            elif c=='L':
                res+=50
            elif c=='C':
                res+=100
            elif c=='D':
                res+=500
            elif c=='M':
                res+=1000
        if 'CD' in s or 'CM' in s:
            res-=200
        if 'XL' in s or 'XC' in s:
            res-=20
        if 'IV' in s or 'IX' in s:
            res-=2
        return res
