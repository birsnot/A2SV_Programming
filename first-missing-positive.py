class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i, n in enumerate(nums):
            while 0 < n <= N and nums[n - 1] != n:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n = nums[i]
        for i, n in enumerate(nums, 1):
            if i != n:
                return i
        return N + 1