class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int R = dungeon.size(), C = dungeon[0].size();
        vector<vector<int>> dp(R, vector<int>(C));
        dp[R - 1][C - 1] = max(1 - dungeon[R - 1][C - 1], 1);
        for(int r = R - 2, c = C - 1; r >= 0; --r)
            dp[r][c] = max(dp[r + 1][c] - dungeon[r][c], 1);
        for(int c = C - 2, r = R - 1; c >= 0; --c)
            dp[r][c] = max(dp[r][c + 1] - dungeon[r][c], 1);
        for(int r = R - 2; r >= 0; --r){
            for(int c = C - 2; c >= 0; --c){
                dp[r][c] = min(max(dp[r + 1][c] - dungeon[r][c], 1), max(dp[r][c + 1] - dungeon[r][c], 1));
            }
        }
        return dp[0][0];
    }
};