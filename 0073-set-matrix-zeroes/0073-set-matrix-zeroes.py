class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if not val:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0