class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        int ans = 0, N = maze.size(), M = maze[0].size();
        queue<pair<int, int>> q;
        int drc[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int r = entrance[0], c = entrance[1];
        maze[r][c] = '+';
        for(const auto& [dr, dc]: drc){
            int nr = r + dr, nc = c + dc;
            if(nr < 0 || nr >= N || nc < 0 || nc >= M || maze[nr][nc] == '+') continue;
            maze[nr][nc] = '+';
            q.push({nr, nc});
        }
        while(!q.empty()){
            int len = q.size();
            ++ans;
            for(int i = 0; i < len; ++i){
                int r = q.front().first, c = q.front().second; q.pop();
                for(const auto& [dr, dc]: drc){
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= N || nc < 0 || nc >= M) return ans;
                    if(maze[nr][nc] == '.'){
                        maze[nr][nc] = '+';
                        q.push({nr, nc});
                    }
                }
            }
        }
        return -1;
    }
};