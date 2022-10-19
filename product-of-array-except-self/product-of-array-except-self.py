class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        L = len(nums)
        ans = [0]*L
        for i,n in enumerate(nums):
            ans[i] = temp
            temp *= n
        temp = 1
        for i in range(L-1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]
        return ans
