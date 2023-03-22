class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ps = list(accumulate(nums, initial=0))
        stk = deque()
        ans = len(nums) + 1
        for i, n in enumerate(ps):
            while stk and n - ps[stk[0]] >= k:
                ans = min(ans, i - stk.popleft())
            while stk and ps[stk[-1]] >= n:
                stk.pop()
            stk.append(i)
        if ans > len(nums):
            return -1
        return ans