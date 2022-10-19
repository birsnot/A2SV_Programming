class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        num_col = len(matrix[0])
        num_row = len(matrix)
        self.sum_matrix = [[0]*num_col for _ in range(num_row)]
        self.sum_matrix[0][0] = matrix[0][0]
        for i in range(1, num_col):
            self.sum_matrix[0][i] = self.sum_matrix[0][i-1] + matrix[0][i]
        for i in range(1, num_row):
            self.sum_matrix[i][0] = self.sum_matrix[i-1][0] + matrix[i][0]
        for r in range(1, num_row):
            for c in range(1, num_col):
                pr = r-1
                pc = c-1
                self.sum_matrix[r][c] = self.sum_matrix[pr][c] + self.sum_matrix[r][pc] - self.sum_matrix[pr][pc] + matrix[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pr = row1-1
        pc = col1-1
        if row1 != 0:
            above = self.sum_matrix[pr][col2]
        else:
            above = 0
        if col1 != 0:
            left = self.sum_matrix[row2][pc]
        else:
            left = 0
        if row1 == 0 or col1 == 0:
            corner = 0
        else:
            corner = self.sum_matrix[pr][pc]
        return self.sum_matrix[row2][col2] - above - left + corner
        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
