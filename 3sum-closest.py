class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target <= -3000: return nums[0] + nums[1] + nums[2]
        if target >= 3000: return nums[-1] + nums[-2] + nums[-3]
        N = len(nums)
        ans = min_diff = 1000000
        for i in range(N):
            for j in range(i + 1, N):
                new_t = target - nums[i] - nums[j]
                idx = bisect_left(nums, new_t, j + 1)
                if idx < N and nums[idx] - new_t < min_diff:
                    ans = nums[i] + nums[j] + nums[idx]
                    min_diff = nums[idx] - new_t
                if idx > j + 1 and new_t - nums[idx - 1] < min_diff:
                    ans = nums[i] + nums[j] + nums[idx - 1]
                    min_diff = new_t - nums[idx - 1]
        return ans