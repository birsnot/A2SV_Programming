class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for cur in nums:
            s = {}
            for prev in dp:
                d = cur - prev
                if d not in dp[prev]:
                    dp[prev][d] = 1
                s[d] = dp[prev][d] + 1
            dp[cur] = s
        return max(max(dp[n].values()) for n in dp)