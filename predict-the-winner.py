class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        s = self.score(nums, 0, len(nums)-1)
        return s >= 0
    
    def score(self, nums, l, r):
        if l == r:
            return nums[l]
        left = nums[l] - self.score(nums, l + 1, r)
        right = nums[r] - self.score(nums, l, r - 1)
        return max(left, right)