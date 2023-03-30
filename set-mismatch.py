class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 0] 
        for i, n in enumerate(nums, 1):
            while i != n:
                if nums[n - 1] != n:
                    if nums[n - 1] != -1:
                        nums[i - 1], nums[n - 1] = nums[n - 1], nums[i - 1]
                        n = nums[i - 1]
                    else:
                        nums[i - 1] = -1
                        nums[n - 1] = n
                        break
                else:
                    nums[i - 1] = -1
                    ans[0] = n
                    break
        for i, n in enumerate(nums, 1):
            if n == -1:
                ans[1] = i
                break
        return ans