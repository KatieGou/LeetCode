class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0 or abs(dividend)<abs(divisor):
            return 0
        current_res=0
        exp_lst=list()
        
        while abs(current_res)+abs(divisor)<=abs(dividend):
            current_res, exp_lst=self.cal_quotient(dividend, divisor, current_res, exp_lst)
            # print(current_res)
            # print(exp_lst)
        
        output=0
        for i in exp_lst:
            output+=2**i
        if dividend*divisor<0:
            output*=-1
        if output<-2**32 or output>2**31-1:
            return 2**31-1
        return output
    
    def cal_quotient(self, dividend, divisor, current_res, exp_lst):
        i=-1
        res=divisor
        old_cur=current_res
        while abs(dividend)-abs(current_res)>=abs(current_res)-abs(old_cur):
            # print('i', i)
            # print('current_res', current_res)
            i+=1
            current_res=old_cur+res
            res+=res
            
        exp_lst.append(i)
        return current_res, exp_lst
