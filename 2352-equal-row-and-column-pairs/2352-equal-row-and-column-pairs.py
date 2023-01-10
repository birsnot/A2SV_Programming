class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        for row in grid:
            r = tuple(row)
            rows[r] = rows.get(r, 0) + 1
        ans = 0
        for col in zip(*grid):
            c = tuple(col)
            ans += rows.get(c, 0)
        return ans
                