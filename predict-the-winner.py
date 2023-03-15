class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def score(nums, l, r):
            if l == r:
                return nums[l]
            left = nums[l] - score(nums, l + 1, r)
            right = nums[r] - score(nums, l, r - 1)
            return max(left, right)
        s = score(nums, 0, len(nums)-1)
        return s >= 0