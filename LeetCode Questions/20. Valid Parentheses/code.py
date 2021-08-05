class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if self.check_complete(stack[-1], c):
                    stack.pop()
                else:
                    stack.append(c)
        if stack:
            return False
        else:
            return True
    
    def check_complete(self, c1, c2):
        if c1=='(' and c2==')':
            return True
        if c1=='[' and c2==']':
            return True
        if c1=='{' and c2=='}':
            return True
        return False
