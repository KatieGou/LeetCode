class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output=list()
        s=''
        left_no, right_no=n, n
        self.DFS(output, s, left_no, right_no)
        return output
    
    def DFS(self, output, s, left_no, right_no):
        if left_no==0 and right_no==0:
            output.append(s)
            return
        if left_no<0 or right_no<0:
            return
        if left_no==right_no:
            self.DFS(output, s+'(', left_no-1, right_no)
        else:
            self.DFS(output, s+'(', left_no-1, right_no)
            self.DFS(output, s+')', left_no, right_no-1)
