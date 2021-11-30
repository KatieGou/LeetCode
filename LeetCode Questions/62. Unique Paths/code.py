class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        graph=[[1]*n]*m
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                graph[r][c]=graph[r+1][c]+graph[r][c+1]
        return graph[0][0]
      
# dynamic programming, buttom up
