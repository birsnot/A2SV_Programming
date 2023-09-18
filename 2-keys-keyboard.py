class Solution:
    def minSteps(self, n: int) -> int:
        dp = list(range(n + 1))
        dp[1] = 0
        for i in range(2, n//2 + 1):
            moves = 2
            for j in range(2*i, n + 1, i):
                dp[j] = min(dp[j], dp[i] + moves)
                moves += 1
        return dp[n]