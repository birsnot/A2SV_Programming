class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0, R = grid.size(), C = grid[0].size();
        function<int(int, int)> dfs = [&](int r, int c){
            grid[r][c] = 0;
            int nr, nc, ret = 1;
            nr = r + 1;
            if (nr < R && grid[nr][c]) ret += dfs(nr, c);
            nr = r - 1;
            if (nr > -1 && grid[nr][c]) ret += dfs(nr, c);
            nc = c + 1;
            if (nc < C && grid[r][nc]) ret += dfs(r, nc);
            nc = c - 1;
            if (nc > -1 && grid[r][nc]) ret += dfs(r, nc);
            return ret;
        };
        for(int r = 0; r < R; ++r)
            for(int c = 0; c < C; ++c)
                if (grid[r][c])
                    ans = max(ans, dfs(r, c));
        return ans;
    }
};