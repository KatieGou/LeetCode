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
        # length=len(s)
        # for i in range(length//2):
        #     if s[i]!=s[length-i-1]:
        #         return False
        # return True
        return s==s[::-1]            
        
