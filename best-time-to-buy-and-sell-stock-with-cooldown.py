class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -prices[0]
        sell = cool = 0
        for n in prices:
            buy = max(buy, cool - n)
            cool = max(cool, sell)
            sell = max(sell, buy + n)
        return max(buy, sell, cool)