class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        i = ans = 0
        j = len(nums)-1
        while i < j:
            temp = sorted_nums[i]+sorted_nums[j]
            if temp > ans: ans = temp
            i += 1
            j -= 1
        return ans
