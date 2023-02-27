class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0
        l = 0
        ans = len(nums) + 1
        for i, n in enumerate(nums):
            sum_ += n
            while sum_ >= target:
                sum_ -= nums[l]
                l += 1
                ans = min(ans, i - l + 2)
        if ans == len(nums) + 1:
            return 0
        return ans