class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans_len = n - 2
        ans = [[0]*(ans_len) for _ in range(ans_len)]
        
        for r in range(ans_len):
            for c in range(ans_len):
                ans[r][c] = max(grid[r][c],grid[r][c + 1],grid[r][c + 2],
                                grid[r + 1][c],grid[r + 1][c + 1],grid[r + 1][c + 2],
                                grid[r + 2][c],grid[r + 2][c + 1],grid[r + 2][c + 2],
                               )
        return ans