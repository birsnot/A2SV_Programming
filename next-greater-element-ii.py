class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        N = len(nums)
        ans = [-1]*N
        for i, n in enumerate(nums):
            while stk and nums[stk[-1]] < n:
                ans[stk.pop()] = n
            stk.append(i)
        for i, n in enumerate(nums):
            while stk and nums[stk[-1]] < n:
                ans[stk.pop()] = n
            if ans[i] == -1:
                stk.append(i)
        return ans