class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        def is3pow(n):
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            return is3pow(n//3)
        return is3pow(n)
