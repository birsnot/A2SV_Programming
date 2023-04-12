class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        N = len(words)
        masks = [0]*N
        for i, w in enumerate(words):
            mask = 0
            for ch in set(w):
                mask |= 1<<(ord(ch) - 97)
            masks[i] = mask
        prev = len(words[1])
        ans = 0
        for i in range(N):
            len1 = len(words[i])
            if len1 < prev:
                break
            for j in range(i + 1, N):
                len2 = len(words[j])
                if len2 < prev:
                    break
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len1*len2)
                    prev = len2
                    break
        return ans