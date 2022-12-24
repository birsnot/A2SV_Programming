class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        
        i = len(nums)-1
        while i > 1:
            two_sum = sorted_nums[i-1] + sorted_nums[i-2]
            if two_sum > sorted_nums[i]:
                return two_sum + sorted_nums[i]
            i -= 1
        return 0