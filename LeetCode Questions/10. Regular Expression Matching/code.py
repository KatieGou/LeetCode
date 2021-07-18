import re
class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        return re.match('^' + p + '$', s)
