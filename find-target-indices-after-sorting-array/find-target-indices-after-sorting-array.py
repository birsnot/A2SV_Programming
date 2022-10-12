class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lower = 0
        count = 0
        for n in nums:
            if n < target:
                lower += 1
            elif n == target:
                count += 1
        ans = [lower + i for i in range(count)]
        return ans
