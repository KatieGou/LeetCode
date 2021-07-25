class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=len(min(strs, key=len))
        prefix=""
        for i in range(min_len):
            pre=strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i]!=pre:
                    return prefix
            prefix+=pre
        return prefix
