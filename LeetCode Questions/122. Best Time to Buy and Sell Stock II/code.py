class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0]*len(prices)
        for i in range(1, len(prices)):
            diff=prices[i]-prices[i-1]
            # print(diff)
            if diff>0:
                dp[i]=dp[i-1]+diff
            else:
                dp[i]=dp[i-1]
        # print(dp)
        if dp[-1]:
            return dp[-1]
        return 0
