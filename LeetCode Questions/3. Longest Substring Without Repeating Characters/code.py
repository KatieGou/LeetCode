class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        all_chars=list(set(s))
        lengths=list()
        for i in range(len(s)):
            chars=list()
            for j in range(i, len(s)):
                if s[j] not in chars:
                    chars.append(s[j])
                else:
                    break
            lengths.append(len(chars))
        if lengths:
            return max(lengths)
        else:
            return 0
