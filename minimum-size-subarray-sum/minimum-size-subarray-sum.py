class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)+1
        ps = [0]*N
        temp = 0
        for i, n in enumerate(nums, 1):
            temp += n
            ps[i] = temp
        if temp < target: return 0
        for j, n in enumerate(ps):
            if n >= target:
                break
        i = 0
        while j < N:
            while ps[j]-ps[i] >= target:
                ans = j-i
                i += 1
            j += 1
            i += 1
        return ans
