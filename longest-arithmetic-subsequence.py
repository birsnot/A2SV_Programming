class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        ans = 0
        for i in range(1, N):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = max(dp[i][d], dp[j][d] + 1)
                ans = max(ans, dp[i][d])
        return ans + 1