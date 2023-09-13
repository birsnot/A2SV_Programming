class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if N < m*k: return -1
        if N == m*k: return max(bloomDay)
        days = sorted(bloomDay)
        if k == 1: return days[m - 1]
        def count(n):
            cnt = ret = 0
            for d in bloomDay:
                if d <= n:
                    cnt += 1
                else:
                    ret += cnt//k
                    cnt = 0
            ret += cnt//k
            return ret
        return days[bisect_left(days, m, key=lambda n: count(n))]