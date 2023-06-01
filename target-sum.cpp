class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum_ = accumulate(nums.begin(), nums.end(), 0);
        if(abs(target) > sum_ || (target + sum_)%2) return 0;
        unordered_map<int, int> dp[nums.size()];
        function<int(int, int)> helper = [&](int i, int target){
            if(dp[i].count(target)) return dp[i][target];
            if(i == 0) return dp[i][target] = (target == nums[i]) + (target == -nums[i]);
            return dp[i][target] = helper(i - 1, target - nums[i]) + helper(i - 1, target + nums[i]);
        };
        return helper(nums.size() - 1, target);
    }
};