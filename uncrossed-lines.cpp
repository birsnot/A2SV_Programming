int dp[501][501];
class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        int N = nums1.size(), M = nums2.size();
        for(int i = 0; i <= N; ++i){
            for(int j = 0; j <= M; ++j){
                if(i == 0 || j == 0) dp[i][j] = 0;
                else if(nums1[i - 1] == nums2[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[N][M];
    }
};