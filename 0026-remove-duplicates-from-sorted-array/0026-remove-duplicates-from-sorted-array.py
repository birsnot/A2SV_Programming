class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0
        for n in nums:
            if n != nums[holder]:
                holder += 1
                nums[holder] = n
        return holder + 1