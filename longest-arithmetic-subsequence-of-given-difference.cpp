class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int dp[20001];
        memset(dp, 0, sizeof(dp));
        for(auto n: arr){
            if(abs(n - difference) <= 10000){
                dp[n + 10000] = max(dp[n + 10000], 1 + dp[n - difference + 10000]);
            }
            else{
                dp[n + 10000] = 1;
            }
        }
        return *max_element(dp, dp + 20001);
    }
};