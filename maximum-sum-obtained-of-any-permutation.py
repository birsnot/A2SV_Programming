class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        line = [0]*(N + 1)
        for st, end in requests:
            line[st] += 1
            line[end + 1] -= 1
        line = sorted(accumulate(line[:-1]))
        ans = 0
        nums.sort()
        for n, m in zip(line, nums):
            ans += n*m
        return ans%(10**9 + 7)