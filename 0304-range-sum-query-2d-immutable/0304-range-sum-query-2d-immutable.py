class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_pre = [list(accumulate(row)) + [0] for row in matrix]
        self.pre = [list(accumulate(col)) + [0] for col in zip(*row_pre)]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[col2][row2] + self.pre[col1-1][row1-1] - self.pre[col1-1][row2] - self.pre[col2][row1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)