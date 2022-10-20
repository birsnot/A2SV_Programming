class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        def f(n):
            if n == 2:
                return (1, 1)
            p = f(n-1)
            return (p[0]+p[1], p[0])
        return f(n)[0]
