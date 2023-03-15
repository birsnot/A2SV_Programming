class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_ = 0
        sums = {}
        sums[0] = 1
        ans = 0
        for n in nums:
            sum_ += n
            check = sum_ - goal
            if check in sums:
                ans += sums[check]
            sums[sum_] = sums.get(sum_, 0) + 1
        return ans