class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for n in stones:
            cur = set()
            for prev in dp:
                cur.add(prev + n)
            dp.update(cur)
        sum_ = sum(stones)
        target = sum_//2
        for i in range(100):
            cur = target - i
            if cur in dp:
                return sum_ - 2*cur