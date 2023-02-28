class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        N = len(nums)
        ans = [0]*N
        for i, n in enumerate(nums):
            ans[i] = prod
            prod *= n
        prod = 1
        for i in range(N - 1, -1, -1):
            ans[i] *= prod
            prod *= nums[i]
        return ans