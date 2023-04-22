class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left <= 2 and right >= 3:
            return [2, 3]

        def isprime(n):
            if n == 1: return False
            if n == 2: return True
            if n%2 == 0: return False
            limit = isqrt(n) + 1
            for i in range(3, limit, 2):
                if n%i == 0: return False
            return True
            
        prev = ans = -right
        min_ = right
        for n in range(left, right+1):
            if isprime(n):
                gap = n - prev
                if gap == 2:
                    return (n - 2, n)
                if gap < min_:
                    min_ = gap
                    ans = n
                prev = n
        if min_ < right:
            return (ans - min_, ans)
        else:
            return (-1, -1)