class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, st, end) -> None:
            while st < end: 
                nums[st], nums[end] = nums[end], nums[st]
                st += 1
                end -= 1
                
        k %= len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0, k-1)
        reverse(nums,k, len(nums)-1)
