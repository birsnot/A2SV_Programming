class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            mid = l + (r - l)//2
            check = mid*mid
            if check <= x:
                l = mid + 1
            else:
                r = mid - 1
        return r