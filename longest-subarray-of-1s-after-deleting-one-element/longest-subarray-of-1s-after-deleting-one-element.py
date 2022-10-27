class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last = -1
        i = -2
        ans = 2
        for j, n in enumerate(nums):
            if n == 0:
                if ans < j-i:
                    ans = j-i
                i, last = last, j
        j += 1
        if ans < j-i:
            ans = j-i
        ans -= 2
        if ans == len(nums):
            return ans-1
        return ans
