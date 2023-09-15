class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis = [[-10**7]]
        dp = [[1]]
        for n in nums:
            if n > lis[-1][-1]:
                idx = len(lis)
                lis.append([n])
                dp.append([0])
            else:
                idx = bisect_left(lis, n, key=lambda x: x[-1])
                lis[idx].append(n)
                dp[idx].append(0)
            for i in range(len(lis[idx - 1]) - 1, -1, -1):
                if lis[idx - 1][i] < n:
                    dp[idx][-1] += dp[idx - 1][i]
                else:
                    break
        return sum(dp[-1])