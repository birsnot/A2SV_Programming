class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = -1
        sum_ = 0
        for j, n in enumerate(nums):
            sum_ += n
            if (j - i)*n - sum_ > k:
                i += 1
                sum_ -= nums[i]
        return j - i
                