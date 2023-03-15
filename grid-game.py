class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        for i in range(1, N):
            grid[0][i] += grid[0][i-1]
        for i in range(N - 2, -1, -1):
            grid[1][i] += grid[1][i+1]
        min_ = grid[0][-1] + grid[1][0]
        for i in range(N):
            check = max(grid[0][-1] - grid[0][i], grid[1][0] - grid[1][i])
            if check < min_:
                min_ = check
        return min_