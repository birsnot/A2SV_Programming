class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        N = len(nums)
        if nums[0] >= N - 1: return 1
        ans = 2
        l = 0
        r = 1
        while True:
            max_ = 0
            max_i = 0
            i = 0
            while r < N and r <= l + nums[l]:
                n = nums[r] + i
                if n > max_:
                    max_ = n
                    max_i = r
                r += 1
                i += 1
            if max_i + nums[max_i] >= N - 1:
                return ans
            l = max_i
            ans += 1