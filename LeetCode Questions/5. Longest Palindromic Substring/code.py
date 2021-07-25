class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        result=""
        for i in range(length):
            for j in range(length, i, -1):
                substring=s[i:j]
                if len(substring)<=len(result):
                    break
                else:
                    if self.check_palindromic(substring):
                        result=substring
                        break
        return result
                
    def check_palindromic(self, s):
        return s==s[::-1]            
        
