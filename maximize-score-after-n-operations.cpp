int dp[1<<14][14];

class Solution {
public:
    int N, ans;
    // unordered_map<int, unordered_map<int, int>> dp;

    int maxScore(vector<int>& nums) {
        N = nums.size();
        ans = 0;
        memset(dp, 0, sizeof dp);
        return backtrack(nums, 0, 1);
    }

    int gcd(int n, int m){
        if(m == 0) return n;
        return gcd(m, n%m);
    }

    
    int backtrack(vector<int>& nums, int mask, int ii){
        if (ii > N) return 0;
        if(dp[mask][ii]) return dp[mask][ii];
        for(int i = 0; i < N; ++i){
            if(((1<<i)&mask) == 0){
                int new_mask = mask | (1<<i);
                for(int j = 0; j < N; ++j){
                    if((new_mask&(1<<j)) == 0){
                        dp[mask][ii] = max(ii*gcd(nums[i], nums[j]) + backtrack(nums, new_mask | (1<<j), ii + 1), dp[mask][ii]);
                    }
                }
            }
        }
        return dp[mask][ii];
    }
};