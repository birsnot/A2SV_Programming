class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 and high%2:
            return (high - low + 2)//2
        else:
            return (high - low + 1)//2