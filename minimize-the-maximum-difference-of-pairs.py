class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        N = len(nums)
        nums.sort()

        def check(n):
            cnt = i = 0
            while i < N - 1:
                if nums[i + 1] - nums[i] <= n:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p
        
        l = r = 0
        for i in range(1, N):
            r = max(r, nums[i] - nums[i - 1])

        while l <= r:
            mid = (l + r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l