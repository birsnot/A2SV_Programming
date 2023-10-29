class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int R = grid.size(), C = grid[0].size();
        for(int r = 1; r < R; ++r) grid[r][0] += grid[r - 1][0];
        for(int c = 1; c < C; ++c) grid[0][c] += grid[0][c - 1];
        for(int r = 1; r < R; ++r){
            for(int c = 1; c < C; ++c){
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1]);
            }
        }
        return grid[R - 1][C - 1];
    }
};