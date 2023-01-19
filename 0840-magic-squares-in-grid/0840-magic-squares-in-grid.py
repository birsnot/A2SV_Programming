class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        fives = []
        for r, row in enumerate(grid[1:-1]):
            for c, val in enumerate(row[1:-1]):
                if val == 5:
                    fives.append((r, c))
        ans = 0
        magic = [1, 6, 7, 2, 9, 4, 3, 8]
        for r, c in fives:
            check = grid[r][c:c + 3] + [grid[r + 1][c + 2]] + grid[r + 2][c:c + 3][::-1] + [grid[r + 1][c]]
            if 1 in check:
                idx = check.index(1)
                check1 = check[idx:] + check[:idx]
                check2 = [1] + check1[1:][::-1]
                if idx%2 and (magic == check1 or magic == check2):
                    ans += 1
        return ans