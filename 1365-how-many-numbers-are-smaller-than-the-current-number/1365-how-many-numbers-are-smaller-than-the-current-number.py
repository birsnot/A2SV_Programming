class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_ = max(nums) + 1
        freq = [0]*max_
        for n in nums:
            freq[n] += 1
        prev = 0
        for i in range(max_):
            val = freq[i]
            freq[i] = prev
            prev += val
        nums_len = len(nums)
        ans = [0]*nums_len
        for i in range(nums_len):
            ans[i] = freq[nums[i]]
        return ans