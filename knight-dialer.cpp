class Solution {
public:
    int knightDialer(int n) {
        long long dp[10], dp2[10];
        for(int i = 0; i < 10; ++i) dp[i] = 1;


        vector<int> nxt[10] = {{4, 6}, {6, 8}, {7, 9}, {4, 8}, {0, 3, 9}, {}, {0, 1, 7}, {2, 6}, {1, 3}, {2, 4}};
        const long long MOD = 1000000007;

        for(int i = 1; i < n; ++i){
            memset(dp2, 0ll, sizeof dp2);
            for(int j = 0; j < 10; ++j){
                for(auto nx: nxt[j]){
                    dp2[nx] += dp[j];
                    dp2[nx] %= MOD;
                }
            }
            swap(dp, dp2);
        }
        return accumulate(dp, dp + 10, 0ll)%MOD;
    }
};