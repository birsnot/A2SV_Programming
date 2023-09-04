class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        left, down, right, up = (0, 1), (1, 0), (0, -1), (-1, 0)
        R = len(grid)
        C = len(grid[0])
        parent_ = [[(r, c) for c in range(C)] for r in range(R)]
        print(parent_)