class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        if(board[click[0]][click[1]] == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }
        int R = board.size(), C = board[0].size();
        int drc[8][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
        function<void(int, int)> dfs = [&](int r, int c){
            board[r][c] = 'B';
            int nr, nc;
            int cur = 0;
            vector<int> next;
            for(int i = 0; i < 8; ++i){
                nr = r + drc[i][0], nc = c + drc[i][1];
                if(nr > -1 && nr < R && nc > -1 && nc < C){
                    if(board[nr][nc] == 'M') ++cur;
                    else if(board[nr][nc] == 'E') next.push_back(i);
                }
            }
            if(cur) board[r][c] = '0' + cur;
            else{
                for(auto i: next) dfs(r + drc[i][0], c + drc[i][1]);
            }
        };
        dfs(click[0], click[1]);
        return board;
    }
};