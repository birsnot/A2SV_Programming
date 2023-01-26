class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k%N
        self.reverse(nums, 0, N - k - 1)
        self.reverse(nums, N - k, N - 1)
        self.reverse(nums, 0, N - 1)
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1