class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = -1
        sum_ = 0
        for n in nums:
            sum_ += n
            if sum_ > x:
                sum_ -= n
                break
            l += 1
        N = len(nums)
        if l == N - 1:
            if sum_ == x:
                return N
            else:
                return -1
        ans = l + 1 if sum_ == x else N
        for r in range(N - 1, 0, -1):
            sum_ += nums[r]
            while sum_ > x and l > -1:
                sum_ -= nums[l]
                l -= 1
            if sum_ == x:
                ans = min(ans, N - r + l + 1)
            elif sum_ > x:
                break
        return ans if ans < N else -1