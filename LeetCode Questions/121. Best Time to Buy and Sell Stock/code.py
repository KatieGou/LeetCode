class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        profits=list()
        while prices:
            future_prices=prices[i+1:]
            try:
                j_=len(future_prices)-1-future_prices[::-1].index(max(future_prices))
                # print(j_)
                j=i+j_+1
                sub_prices=prices[i:j]
                profits.append(prices[j]-min(sub_prices))
                prices=prices[j+1:]
            except:
                break
        
        # print(profits)
        if profits:
            if max(profits)>0:
                return max(profits)
        return 0
