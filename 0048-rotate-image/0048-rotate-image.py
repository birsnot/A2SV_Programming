class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat_len = len(matrix)
        n = mat_len - 1
        for diag in range(mat_len//2):
            r = c = diag
            loops = n - 2*diag
            for i in range(loops):
                r = diag
                c = diag + i
                prev = matrix[n-c][r]
                for _ in range(4):
                    val = prev
                    prev = matrix[r][c]
                    matrix[r][c] = val
                    r, c = (c , n - r)