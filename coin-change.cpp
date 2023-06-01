class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int dp[amount + 1];
        for(int i = 1; i <= amount; ++i) dp[i] = 10001;
        dp[0] = 0;
        sort(coins.begin(), coins.end());
        for(int i = 1; i <= amount; ++i){
            for(auto c: coins){
                if(c < i){
                    if(dp[i - c] != 10001) dp[i] = min(dp[i], 1 + dp[i - c]);
                }
                else {
                    if(i == c) dp[i] = 1;
                    break;
                }
            }
        }
        if(dp[amount] > 10000) return -1;
        return dp[amount];
    }
};