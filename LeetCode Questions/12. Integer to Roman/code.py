class Solution:
    def intToRoman(self, num: int) -> str:
        s=str(num)
        l=len(s)
        res=''
        for i in range(l):
            n=int(s[l-i-1])*(10**i)
            print(n)
            res=self.symbol(n)+res
        return res
    
    def symbol(self, value):
        if value==0:
            return ''
        if value<10:
            if value==5:
                return 'V'
            elif value<5:
                if value==4:
                    return 'IV'
                else:
                    s=''
                    for i in range(value):
                        s+='I'
                    return s
            else:
                if value==9:
                    return 'IX'
                else:
                    s='V'
                    for i in range(value-5):
                        s+='I'
                    return s
        elif value<100:
            if value==10:
                return 'X'
            elif value==50:
                return 'L'
            elif value<50:
                if value==40:
                    return 'XL'
                else:
                    s=''
                    for i in range(value//10):
                        s+='X'
                    return s
            else:
                if value==90:
                    return 'XC'
                else:
                    s='L'
                    for i in range((value-50)//10):
                        s+='X'
                    return s
        elif value<1000:
            if value==100:
                return 'C'
            elif value==500:
                return 'D'
            elif value<500:
                if value==400:
                    return 'CD'
                else:
                    s=''
                    for i in range(value//100):
                        s+='C'
                    return s
            else:
                if value==900:
                    return 'CM'
                else:
                    s='D'
                    for i in range((value-500)//100):
                        s+='C'
                    return s
        else:
            s=''
            for i in range(value//1000):
                s+='M'
            return s
