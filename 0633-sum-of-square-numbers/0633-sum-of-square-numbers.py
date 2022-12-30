class Solution:
    def __init__(self):
        self.squares = {}
        for n in range(46341):
            self.squares[n*n] = 0
            
    def judgeSquareSum(self, c: int) -> bool:
        loops = int(sqrt(c)) + 1
        p = iter(self.squares)
        for i in range(loops):
            a2 = next(p)
            b2 = c - a2
            if b2 in self.squares:
                return True
        return False