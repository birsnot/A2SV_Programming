class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calcD(n):
            day = 1
            temp = 0
            for w in weights:
                temp += w
                if temp > n:
                    day += 1
                    temp = w
            return day
        l = max(weights)
        r = l*len(weights)
        while l <= r:
            mid = (l + r)//2
            if calcD(mid) > days:
                l = mid + 1
            else:
                r = mid - 1
        return l