class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i//2):
                dp[i] += dp[i - 1 - j]*dp[j]*2
            if i%2:
                dp[i] += dp[i//2]*dp[i//2]
        return dp[n]