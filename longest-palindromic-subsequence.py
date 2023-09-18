class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0]*N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for i in range(1, N):
            for l in range(N - i):
                r = l + i
                if s[r] == s[l]:
                    dp[l][r] = 2 + dp[l + 1][r - 1]
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        return dp[0][N - 1]