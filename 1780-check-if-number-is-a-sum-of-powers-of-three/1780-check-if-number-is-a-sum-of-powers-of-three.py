class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power3 = []
        for i in range(14, -1, -1):
            power3.append(3**i)
        for p in power3:
            if p <= n:
                n -= p
            if n == 0:
                return True
        return False