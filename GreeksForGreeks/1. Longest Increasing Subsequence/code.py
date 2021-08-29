# Description: Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp=[1]*n
        for i in range(1, n):
            idx=None
            length=0
            changed=False
            for j in range(i):
                if a[j]<a[i] and dp[j]>length:
                    idx=j
                    changed=True
                    length=dp[j]
            if changed:
                dp[i]=dp[idx]+1
        # print(dp)
        return max(dp)
      
# dp programming
# dp[i] means the longest subseqence length at index i.
# dp is initialized to a list containing 1s with length n
# i is the index currently focusing on, its value depends on the previous value a[j] which satisfies two conditions:
# 1. a[j] < a[i]
# 2. dp[j] should be as big as possible
# If such j is found, update dp[i] using dp[i]=dp[j]+1.
# Finally, return the largest value from dp. 
