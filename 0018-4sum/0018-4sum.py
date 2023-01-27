class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = set()
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:],i+1):
                k = target - n - m
                left = 0
                right = N - 1
                while left < right:
                    sum_ = nums[left] + nums[right]
                    if sum_ < k:
                        left += 1
                    elif sum_ > k:
                        right -= 1
                    else:
                        if left == i or left == j or right == i or right == j:
                            if left == i or left == j:
                                left += 1
                            else:
                                right -= 1
                            continue
                        temp = tuple(sorted([n, m, nums[left], nums[right]]))
                        ans.add(temp)
                        left += 1
                        right -= 1
        return ans