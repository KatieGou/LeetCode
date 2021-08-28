from collections import Counter
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for lst in board:
            if not self.check_valid(lst):
                return False
        for i in range(len(board[0])):
            board=np.array(board)
            lst=board[:, i]
            if not self.check_valid(lst):
                return False
        for r1 in range(0, 9, 3):
            r2=r1+3
            for c1 in range(0, 9, 3):
                c2=c1+3
                lst=board[r1:r2, c1:c2].flatten()
                if not self.check_valid(lst):
                    return False
        return True
    
    def check_valid(self, lst):
        # print(lst)
        cnt=dict(Counter(lst))
        # print(cnt)
        cnt.pop(".")
        # print('cnt after', cnt)
        cnt=list(cnt.values())
        cnt.sort(reverse=True)
        # print(cnt)
        if cnt:
            if cnt[0]>1:
                return False
            else:
                return True
        else:
            return True
