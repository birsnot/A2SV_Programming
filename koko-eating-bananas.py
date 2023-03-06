class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(k):
            ans = 0
            for n in piles:
                ans += ceil(n/k)
            return ans <= h

        l = 1
        r = max(piles)
        while l <= r:
            mid = (r + l)//2
            check = finish(mid)
            if check:
                r = mid - 1
            else:
                l = mid + 1
        return l