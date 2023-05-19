class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size() - 1;
        if(grid[0][0] || grid[n][n]) return -1;
        queue<pair<int, int>> q; q.push({0, 0});
        grid[0][0] = 1;
        int ans = 0;
        int len, r, c, nr, nc;
        int drc[8][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}};
        while(!q.empty()){
            len = q.size();
            ++ans;
            for(int i = 0; i < len; ++i){
                r = q.front().first, c = q.front().second; q.pop();
                if(r == n && c == n) return ans;
                for(const auto& [dr, dc]: drc){
                    nr = r + dr; nc = c + dc;
                    if(nr < 0 || nr > n || nc < 0 || nc > n || grid[nr][nc]) continue;
                    grid[nr][nc] = 1;
                    q.push({nr, nc});
                }
            }
        }
        return -1;
    }
};