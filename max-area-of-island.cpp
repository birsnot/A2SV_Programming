class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0, R = grid.size(), C = grid[0].size();
        vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        function<int(int, int)> dfs = [&](int r, int c){
            grid[r][c] = 0;
            int ret = 1;
            for(auto d: dir){
                int nr = r + d.first;
                int nc = c + d.second;
                if (nr > -1 && nc > -1 && nr < R && nc < C and grid[nr][nc]) ret += dfs(nr, nc);
            }
            return ret;
        };
        for(int r = 0; r < R; ++r)
            for(int c = 0; c < C; ++c)
                if (grid[r][c])
                    ans = max(ans, dfs(r, c));
        return ans;
    }
};