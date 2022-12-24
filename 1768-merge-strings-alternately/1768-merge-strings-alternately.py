class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        len_word1 = len(word1)
        len_word2 = len(word2)
        ans = ""
        while i < len_word1 and i < len_word2:
            ans += word1[i] + word2[i]
            i += 1
        if i < len_word1:
            ans += word1[i:]
        elif i < len_word2:
            ans += word2[i:]
        return ans