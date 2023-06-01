class Solution {
public:
    int uniquePaths(int m, int n) {
        int grid[m + 1][n + 1];
        for(int r = 0; r <= m; ++r) grid[r][0] = 0;
        for(int c = 0; c <= n; ++c) grid[0][c] = 0;
        grid[0][1] = 1;
        for(int r = 1; r <= m; ++r)
            for(int c = 1; c <= n; ++c){
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1];
            }
        return grid[m][n];
    }
};