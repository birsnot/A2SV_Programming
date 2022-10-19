class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0]*101
        ans = 0
        for n in nums:
            ans += count[n]
            count[n] += 1
        return ans
