class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        N = nums_len-1
        for i in range(N):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        cur = 0
        for n in nums:
            if n:
                nums[cur] = n
                cur += 1
        while cur < nums_len:
            nums[cur] = 0
            cur += 1
        return nums