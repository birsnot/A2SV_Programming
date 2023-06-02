class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int N = questions.size();
        long long dp[N];
        memset(dp, 0, sizeof(dp));
        long long prev = 0;
        for(int i = 0; i < N; ++i){
            prev = max(prev, dp[i]);
            dp[i] = prev + questions[i][0];
            int next = i + questions[i][1] + 1;
            if(next < N) dp[next] = max(dp[next], dp[i]);
        }
        return *max_element(dp, dp + N);
    }
};