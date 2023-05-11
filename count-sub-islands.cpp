class Solution {
public:
    int drc[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int R, C;
    bool dfs(int r, int c, vector<vector<int>>& grid1, vector<vector<int>>& grid2){
        grid2[r][c] = 0;
        int nr, nc;
        bool ret = grid1[r][c];
        for(auto d: drc){
            nr = r + d[0], nc = c + d[1];
            if(nr < 0 || nr == R || nc < 0 || nc == C) continue;
            if(grid2[nr][nc]){
                ret = dfs(nr, nc, grid1, grid2) && grid1[nr][nc] && ret;
            }
        }
        return ret;
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        R = grid1.size(), C = grid1[0].size();
        int ans = 0;
        for(int r = 0; r < R; ++r)
            for(int c = 0; c < C; ++c)
                if(grid2[r][c])
                    ans += dfs(r, c, grid1, grid2);
        return ans;
    }
};