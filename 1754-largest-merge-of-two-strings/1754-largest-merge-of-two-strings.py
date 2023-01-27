class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        p1 = 0
        p2 = 0
        ans = []
        while p1 < len1 and p2 < len2:
            if word1[p1:] > word2[p2:]:
                ans.append(word1[p1])
                p1 += 1
            else:
                ans.append(word2[p2])
                p2 += 1
        return "".join(ans) + word1[p1:] + word2[p2:]