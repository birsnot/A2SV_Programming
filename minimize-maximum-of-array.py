class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sum_ = 0
        ans = 0
        for i, n in enumerate(nums, 1):
            sum_ += n
            if n > ans:
                ans = max(ans, -(-sum_//i))
        return ans