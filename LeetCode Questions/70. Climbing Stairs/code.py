class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        dic={1:1, 2:2}
        for level in range(3, n+1):
            dic[level]=dic[level-1]+dic[level-2]
        return dic[n]

# another solution but time excceed
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
