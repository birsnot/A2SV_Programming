class Solution:
    def isHappy(self, n: int) -> bool:
        prev_n = n
        while True:
            new_n = sum(map(self.sq, list(str(prev_n))))
            if new_n == 4:
                return False
            if new_n == 1:
                return True
            prev_n = new_n
    
    def sq(self, n: str) -> int:
        return int(n)**2