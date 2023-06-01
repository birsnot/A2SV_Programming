class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() < 4) return *max_element(nums.begin(), nums.end());
        int cur, prev1 = 0, prev2 = nums[0];
        for(int i = 1; i < nums.size() - 1; ++i){
            cur = max(prev1 + nums[i], prev2);
            prev1 = prev2;
            prev2 = cur;
        }
        int ans = cur;
        prev1 = 0, prev2 = nums[1];
        for(int i = 2; i < nums.size(); ++i){
            cur = max(prev1 + nums[i], prev2);
            prev1 = prev2;
            prev2 = cur;
        }
        return max(cur, ans);
    }
};