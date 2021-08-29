class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s)
        # print(dp)
        max_len=0
        for i in range(1, len(s)):
            if s[i]==')':
                if s[i-1]=='(': # form a new '()', length+=2
                    if i>=2:
                        dp[i]=dp[i-2]+2
                    else:
                        dp[i]=2
                else:
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(': # continuous
                        if i-dp[i-1]-2>=0:
                            dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2 # len of substr just before it + len of str before the current str + newly added str
                        else:
                            dp[i]=dp[i-1]+2
                max_len=max(max_len, dp[i])
        return max_len
