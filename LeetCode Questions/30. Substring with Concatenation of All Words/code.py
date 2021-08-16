from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_num=dict(Counter(words))
        # print(words_num)
        total_char=len(words)*len(words[0])
        len_words=len(words)
        len_word=len(words[0])
        idx_lst=list()
        i=0
        j=i+total_char
        while j<=len(s):
            chunks=[s[i+k:i+k+len_word] for k in range(0, total_char, len_word)]
            current=dict(Counter(chunks))
            # print(current)
            if current==words_num:
                idx_lst.append(i)
            i+=1
            j=i+total_char
        return idx_lst
