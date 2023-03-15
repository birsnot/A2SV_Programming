class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = sum_ = 0
        sums = defaultdict(int)
        sums[0] = 1
        for n in nums:
            sum_ += n
            ans += sums[sum_ - goal]
            sums[sum_] += 1
        return ans