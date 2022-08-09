class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0 for i in range(n)] for j in range(n)]
        pos_lst=list()
        c_left, c_right=0, n
        r_up, r_down=0, n
        i=0
        while len(pos_lst)<n*n:
            if i%2==0:
                if i%4==0: # right
                    for p in range(c_left, c_right):
                        pos_lst.append((r_up, p))
                    r_up+=1
                else: # left
                    for p in range(c_right-1, c_left-1, -1):
                        pos_lst.append((r_down-1, p))
                    r_down-=1
            else:
                if (i+1)%4==0: # up
                    for p in range(r_down-1, r_up-1, -1):
                        pos_lst.append((p, c_left))
                    c_left+=1
                else: # down
                    for p in range(r_up, r_down):
                        pos_lst.append((p, c_right-1))
                    c_right-=1
            i+=1
        # print(pos_lst)
        for index in range(n*n):
            pos=pos_lst[index]
            res[pos[0]][pos[1]]=index+1
        return res
