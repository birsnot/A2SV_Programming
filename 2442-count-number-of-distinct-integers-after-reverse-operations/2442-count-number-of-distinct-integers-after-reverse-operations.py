class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for n in nums:
            nums_set.add(int(str(n)[::-1]))
        return len(nums_set)