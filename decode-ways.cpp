class Solution {
public:
    int numDecodings(string s) {
        if(s[0] == '0') return 0;
        int N = s.size();
        unsigned int dp[N + 1];
        memset(dp, 0, sizeof(dp));
        dp[0] = 1; dp[1] = 1;
        int d1 = s[0] - '0', d0;
        for(int i = 1; i < N; ++i){
            d0 = s[i] - '0';
            if(d0){
                dp[i + 1] = dp[i];
                if(d1 && d1*10 + d0 < 27) dp[i + 1] += dp[i - 1];
            }
            else{
                if(d1 && d1 < 3) dp[i + 1] = dp[i - 1];
                else return 0;
            }
            d1 = d0;
        }
        return dp[N];
    }
};