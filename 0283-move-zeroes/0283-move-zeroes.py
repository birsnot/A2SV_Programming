class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        for n in nums:
            if n != 0:
                nums[current] = n
                current += 1
        nums_len = len(nums)
        while current < nums_len:
            nums[current] = 0
            current += 1