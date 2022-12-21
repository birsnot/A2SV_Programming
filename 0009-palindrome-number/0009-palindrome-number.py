class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        q = x
        y = 0
        while q:
            y = y*10 + q%10
            q = q//10
        return x == y