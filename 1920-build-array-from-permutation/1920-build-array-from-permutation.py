class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0]*nums_len
        i = 0 
        while i < nums_len:
            ans[i] = nums[nums[i]]
            i += 1
        return ans