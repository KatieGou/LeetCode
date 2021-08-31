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
    
# my solution 2 (more efficient): 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for i in range(1, len(prices)):
            profit=prices[i]-min_price
            if prices[i]<min_price:
                min_price=prices[i]
            if profit>0 and profit>max_profit:
                max_profit=profit
        if max_profit:
            return max_profit
        return 0
