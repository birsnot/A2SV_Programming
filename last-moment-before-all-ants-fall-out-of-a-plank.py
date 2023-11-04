class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans1 = ans2 = -1
        if left: ans1 = max(left)
        if right: ans2 = n - min(right)
        return max(ans1, ans2)