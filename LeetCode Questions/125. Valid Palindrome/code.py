class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=''
        for s_ in s:
            if s_.isalpha() or s_.isnumeric():
                clean_s+=s_.lower()
        
        if clean_s==clean_s[::-1]:
            return True
        return False
