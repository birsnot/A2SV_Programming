class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        binary = bin(n)
        if binary.count("1") == 1 and (len(binary) - binary.index("1") - 1)%2 == 0:
            return True
        return False