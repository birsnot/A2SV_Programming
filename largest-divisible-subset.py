class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = {}
        nums.sort()
        for n in nums:
            cur = [0, -1]
            for prev in dp:
                if n%prev == 0 and dp[prev][0] > cur[0]:
                    cur[0] = dp[prev][0]
                    cur[1] = prev
            cur[0] += 1
            dp[n] = cur
        ans = [max(dp, key=lambda k: dp[k])]
        while dp[ans[-1]][1] != -1:
            ans.append(dp[ans[-1]][1])
        return ans