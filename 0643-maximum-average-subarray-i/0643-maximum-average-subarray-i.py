class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = sum_ = sum(nums[:k])
        for i, n in enumerate(nums[k:]):
            sum_ += n - nums[i]
            if sum_ > max_:
                max_ = sum_
        return max_/k