class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        return self.helper(n)
    
    def helper(self, n):
        if n == 1: return True
        if n%4: return False
        return self.helper(n//4)