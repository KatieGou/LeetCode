class Solution:
    def exist(self, board, word: str) -> bool:
        m, n=len(board), len(board[0])
        l_word=len(word)

        def dfs(r, c, cur):
            if cur==l_word: # final: when cur out of range of word
                return True
            if r<0 or r>=m or c<0 or c>=n or word[cur]!=board[r][c]:
                return False
            # continue when neither return true or false
            board[r][c]=0 # modify traversed cell 
            res=dfs(r+1, c, cur+1) or dfs(r-1, c,cur+1) or dfs(r, c+1, cur+1) or dfs(r, c-1, cur+1)
            board[r][c]=word[cur] # recover traversed cell
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
