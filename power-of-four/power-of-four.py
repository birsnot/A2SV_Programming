class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        while True:
            if n == 1:
                return True
            elif n & 3:
                return False
            else:
                n >>= 2
