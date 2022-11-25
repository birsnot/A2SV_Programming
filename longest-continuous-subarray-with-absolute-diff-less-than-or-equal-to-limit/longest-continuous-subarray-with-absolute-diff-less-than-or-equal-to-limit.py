class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        mn = mx = nums[0]
        ans = i_mx = i_mn = k = i = 0
        while i < n:
            if nums[i] <= mn:
                mn = nums[i]
                i_mn = i
                while mx-mn > limit:
                    k = j = i_mx + 1
                    mx = mn
                    i_mx = i_mn
                    while j < i_mn:
                        if nums[j] >= mx:
                            mx = nums[j]
                            i_mx = j
                        j += 1
            elif nums[i] >= mx:
                mx = nums[i]
                i_mx = i
                while mx-mn > limit:
                    k = j = i_mn + 1
                    mn = mx
                    i_mn = i_mx
                    while j < i_mx:
                        if nums[j] <= mn:
                            mn = nums[j]
                            i_mn = j
                        j += 1
            i += 1
            temp = i - k
            if temp > ans: ans = temp
        return ans
