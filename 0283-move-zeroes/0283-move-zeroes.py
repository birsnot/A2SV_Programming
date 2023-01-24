class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
        for seeker, num in enumerate(nums):
            if num:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                placeholder += 1