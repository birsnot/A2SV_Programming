class Solution:
    def minSteps(self, n: int) -> int:
        fact = []
        i = 2
        while i*i <= n:
            while n%i == 0:
                fact.append(i)
                n //= i
            i += 1
        if n > 1:
            fact.append(n)
        return sum(fact)