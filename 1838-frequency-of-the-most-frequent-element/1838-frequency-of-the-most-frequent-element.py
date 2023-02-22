class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ps = [0] + list(accumulate(nums))
        i = 0
        for j, n in enumerate(ps[1:], 1):
            if nums[j - 1]*(j-i) - n + ps[i] > k:
                i += 1
        return j - i
                