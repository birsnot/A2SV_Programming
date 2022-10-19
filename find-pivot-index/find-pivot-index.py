class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = [0]
        for n in nums:
            ps.append(ps[-1] + n)
        for i,n in enumerate(nums):
            if ps[i] == ps[-1] - ps[i+1]:
                return i
        return -1
