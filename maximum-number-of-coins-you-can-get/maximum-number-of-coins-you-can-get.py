class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles,reverse=True)
        n = len(piles)//3
        ans = 0
        i = 1
        for _ in range(n):
            ans += piles[i]
            i += 2
        return ans
