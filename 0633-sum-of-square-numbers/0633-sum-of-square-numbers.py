class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(sqrt(c))
        left = 0
        while left <= right:
            sum_ = left**2 + right**2
            if sum_ == c:
                return True
            elif sum_ > c:
                right -= 1
            else:
                left += 1
        return False