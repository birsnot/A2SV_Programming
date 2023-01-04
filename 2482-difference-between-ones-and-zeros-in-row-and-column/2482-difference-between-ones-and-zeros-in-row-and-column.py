class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row_sums = [0]*m
        for i, row in enumerate(grid):
            zero_one = [0,0]
            for col in row:
                zero_one[col] += 1
            row_sums[i] = zero_one
        
        col_sums = [0]*n
        for col in range(n):
            zero_one = [0,0]
            for row in range(m):
                zero_one[grid[row][col]] += 1
            col_sums[col] = zero_one
        
        ans = [[0]*n for _ in range(m)]
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                ans[r][c] = row_sums[r][1] + col_sums[c][1] - row_sums[r][0] - col_sums[c][0]
        return ans