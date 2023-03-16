class Solution:
    def hIndex(self, cts: List[int]) -> int:
        N = len(cts)
        def check(i):
            h = N - i
            return cts[i] >= h
        l = 0
        r = N - 1
        while l <= r:
            mid = (l + r)>>1
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return N - l