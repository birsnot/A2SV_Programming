class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        queue<pair<int, int>> q;
        int N = mat.size(), M = mat[0].size();
        vector<vector<int>> visited(N, vector<int> (M));
        for(int r = 0; r < N; ++r)
            for(int c = 0; c < M; ++c)
                if(mat[r][c] == 0){
                    visited[r][c] = 1;
                    q.push({r, c});
                }
        int dis = 0;
        int drc[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        while(!q.empty()){
            int len = q.size();
            ++dis;
            for(int i = 0; i < len; ++i){
                int r = q.front().first, c = q.front().second; q.pop();
                for(const auto& [dr, dc]: drc){
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                    if(visited[nr][nc] == 0){
                        visited[nr][nc] = 1;
                        mat[nr][nc] = dis;
                        q.push({nr, nc});
                    }
                }
            }
        }
        return mat;
    }
};