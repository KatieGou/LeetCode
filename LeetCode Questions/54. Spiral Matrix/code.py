class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n=len(matrix), len(matrix[0])
        res=list()
        i=0
        m_up, m_down=0, m
        n_left, n_right=0, n
        while len(res)<m*n:
            print(res)
            if i%2==0:
                if i%4==0: # n_ increases
                    for n_ in range(n_left, n_right):
                        res.append(matrix[m_up][n_])
                    m_up+=1
                else: # n decreases
                    for n_ in range(n_right-1, n_left-1, -1):
                        res.append(matrix[m_down-1][n_])
                    m_down-=1
            else:
                if (i-1)%4==0: # m_ increases
                    for m_ in range(m_up, m_down):
                        res.append(matrix[m_][n_right-1])
                    n_right-=1
                else: # m_decreases
                    for m_ in range(m_down-1, m_up-1, -1):
                        res.append(matrix[m_][n_left])
                    n_left+=1
            i+=1
        return res
