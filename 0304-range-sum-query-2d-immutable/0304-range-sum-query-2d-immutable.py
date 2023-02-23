class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        self.pre = [[0]*cols for _ in range(rows)]
        for r in range(1, rows):
            for c in range(1, cols):
                self.pre[r][c] = self.pre[r-1][c] + self.pre[r][c-1] - self.pre[r-1][c-1] + matrix[r-1][c-1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r2 = row2 + 1
        c2 = col2 + 1
        return self.pre[r2][c2] + self.pre[row1][col1] - self.pre[row1][c2] - self.pre[r2][col1]
        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)