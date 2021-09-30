class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n=len(board), len(board[0])
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n or board[r][c]=='X':
                return
            if board[r][c]=='O':
                board[r][c]='U' # 'U' means unchange
                for d in directions:
                    dfs(r+d[0], c+d[1])
        for r in range(m):
            dfs(r, 0)
            dfs(r, n-1)
        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='U':
                    board[r][c]='O'
