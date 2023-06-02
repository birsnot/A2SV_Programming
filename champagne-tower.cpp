class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        vector<double> dp(1, poured);
        for(int i = 0; i < query_row; ++i){
            double prev = 0;
            for(int j = 0; j <= i; ++j){
                double cur = (max(0.0, dp[j] - 1.0))/2;
                dp[j] = prev + cur;
                prev = cur;
            }
            dp.push_back(prev);
        }
        return min(dp[query_glass], 1.0);
    }
};