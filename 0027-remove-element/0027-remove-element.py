class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        for n in nums:
            if n != val:
                nums[current] = n
                current += 1
        return current