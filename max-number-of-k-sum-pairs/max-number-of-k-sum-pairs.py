class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        ans = 0
        while i < j:
            n = k - nums[i]
            while nums[j] > n and j > i:
                j -= 1
            if nums[j] == n and j != i:
                ans += 1
                j -= 1
            i += 1
        return ans
