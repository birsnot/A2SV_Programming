class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0: return 1
        if x == 0: return 0
        def power(x, n):
            if n == 1: return x
            return power(x*x, n//2)*[1, x][n%2]
        if n < 0:
            return 1/power(x, -n)
        return power(x, n)