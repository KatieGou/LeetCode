class Solution:
    def longestPalindrome(self, s: str) -> int:
        unique=list(set(s))
        length=0
        flag=False
        for l in unique:
            count=s.count(l)
            if count%2==0:
                length+=count
            else:
                length+=count-1
                flag=True
        if flag:
            length+=1
        return length

# If a Palindrome sequence has a center, the number of the center letter must be odd. If not, all numbers should be even.
