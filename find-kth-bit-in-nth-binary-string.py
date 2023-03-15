class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k, b):
            if k == 1:
                return str(b)
            mid = 2**(n - 1)
            if k > mid:
                return helper(n - 1, 2*mid - k, b^1)
            elif k < mid:
                return helper(n - 1, k, b)
            else:
                return str(b^1)
        return helper(n, k, 0)