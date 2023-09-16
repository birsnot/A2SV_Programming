class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2: return False
        dp = {0}
        for n in nums:
            cur = set()
            for prev in dp:
                cur.add(prev + n)
            dp.update(cur)
        return (total//2) in dp