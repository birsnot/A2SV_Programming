class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        mins = [0]*N
        min_ = nums[0]
        for i,n in enumerate(nums):
            if n < min_:
                min_ = n
            mins[i] = min_
        stk = []
        for i in range(N - 1, 0, -1):
            if stk and mins[i] < stk[-1] < nums[i]:
                return True
            stk.append(nums[i])
            while stk and stk[-1] <= mins[i-1]:
                stk.pop()
        return False