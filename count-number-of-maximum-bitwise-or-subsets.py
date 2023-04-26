class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = mx = 0
        N = len(nums)
        for n in nums:
            mx |= n
        def bt(i, cur):
            if i == N: return
            nonlocal ans
            bt(i + 1, cur)
            cur |= nums[i]
            if cur == mx:
                ans += 1
            bt(i + 1, cur)
        bt(0, 0)
        return ans