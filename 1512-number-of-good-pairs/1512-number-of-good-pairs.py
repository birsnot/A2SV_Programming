class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict = {}
        ans = 0
        for n in nums:
            if n in nums_dict:
                ans += nums_dict[n]
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1
        return ans