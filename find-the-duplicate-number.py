class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            while nums[n - 1] != n:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n = nums[i]
            if n != i + 1: return n