class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        for cur in nums:
            cnt = 0
            for prev in dp:
                if prev < cur and dp[prev] > cnt:
                    cnt = dp[prev]
            dp[cur] = 1 + cnt
        return max(dp.values())