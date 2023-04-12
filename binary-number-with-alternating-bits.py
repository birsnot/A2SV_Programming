class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m = n&-n
        if m > 2: return False
        n -= m
        while n > 0:
            m <<= 2
            if n&-n != m: return False
            n -= m
        return True