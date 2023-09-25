from sortedcontainers import SortedList
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(ages,scores))
        dp = {}
        for _, sc in arr:
            cur = 0
            for prev in dp:
                if prev <= sc:
                    cur = max(cur, dp[prev])
            dp[sc] = cur + sc
        return max(dp.values())