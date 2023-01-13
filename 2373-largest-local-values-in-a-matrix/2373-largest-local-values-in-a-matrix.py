class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans_len = n - 2
        ans = [[0]*(ans_len) for _ in range(ans_len)]
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                r_left = max(0, r - 2)
                r_right = min(ans_len, r + 1)
                c_left = max(0, c - 2)
                c_right = min(ans_len, c + 1)
                for r_ in range(r_left, r_right):
                    for c_ in range(c_left, c_right):
                        ans[r_][c_] = max(ans[r_][c_], val)
        return ans
                
        