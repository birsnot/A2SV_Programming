class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        prev = [[1]*n for _ in range(n)]
        cur = [[0]*n for _ in range(n)]
        drc = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
        for _ in range(k):
            for r in range(n):
                for c in range(n):
                    cur_val = 0
                    for dr, dc in drc:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            cur_val += prev[nr][nc]
                    cur[r][c] = cur_val/8
            cur, prev = prev, cur
        return prev[row][column]