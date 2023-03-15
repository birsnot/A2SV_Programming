class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(k, b):
            if k == 1:
                return b
            return helper((k + 1)//2, [[1, 0], [0, 1]][k%2][b])
        return helper((k + 1)//2, 0)^[1, 0][k%2]