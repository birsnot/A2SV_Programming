class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        for r in range(N - 1):
            for c in range(N):
                min_ = matrix[r][c]
                if c > 0:
                    min_ = min(min_, matrix[r][c - 1])
                if c < N - 1:
                    min_ = min(min_, matrix[r][c + 1])
                matrix[r + 1][c] += min_
        return min(matrix[N - 1])