class Solution {
public:
    void solve(vector<vector<char>>& board) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        N = board.size(); M = board[0].size();
        vector<vector<int>> visited(N, vector<int> (M));
        for(int r = 0; r < N; ++r)
            for(auto c: {0, M - 1})
                if(board[r][c] == 'O' && visited[r][c] == 0) {
                    visited[r][c] = 1;
                    dfs(board, visited, r, c);
                }
        for(int c = 1; c < M - 1; ++c)
            for(auto r: {0, N - 1})
                if(board[r][c] == 'O' && visited[r][c] == 0) {
                    visited[r][c] = 1;
                    dfs(board, visited, r, c);
                }
        for(int r = 1; r < N - 1; ++r)
            for(int c = 1; c < M - 1; ++c)
                if(board[r][c] == 'O' && visited[r][c] == 0) board[r][c] = 'X';
    }
    void dfs(vector<vector<char>>& board, vector<vector<int>>& visited, int r, int c){
        int nr, nc;
        for(const auto& [dr, dc]: drc){
            nr = r + dr; nc = c + dc;
            if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if(board[nr][nc] == 'O' && visited[nr][nc] == 0){
                visited[nr][nc] = 1;
                dfs(board, visited, nr, nc);
            }
        }
    }
    int drc[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int N, M;
};