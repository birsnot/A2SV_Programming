class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                z = i
                break
        i += 1
        while i < len(nums):
            if nums[i] != 0:
                nums[z] = nums[i]
                nums[i] = 0
                z += 1
            i += 1
