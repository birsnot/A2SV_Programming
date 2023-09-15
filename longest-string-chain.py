class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words.sort(key=lambda w: len(w))
        for w in words:
            cur = 0
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                cur = max(cur, dp.get(prev, 0))
            dp[w] = cur + 1
        return max(dp.values())