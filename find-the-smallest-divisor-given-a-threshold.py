class Solution:
    def smallestDivisor(self, nums: List[int], tr: int) -> int:
        def check(i):
            ret = 0
            for n in nums:
                ret += -n//i
            return -ret <= tr
        l = 1
        r = max(nums)
        while l <= r:
            mid = (r + l)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l