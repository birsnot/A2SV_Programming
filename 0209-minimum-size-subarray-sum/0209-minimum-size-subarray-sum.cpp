class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        long sum_ = 0;
        int l = 0, ans = nums.size() + 1;
        for (int i = 0; i < nums.size(); ++i){
            sum_ += nums[i];
            while(sum_ >= target){
                sum_ -= nums[l];
                ans = min(ans, i - l + 1);
                l += 1;
            }
        }
        if(ans == nums.size() + 1){
            return 0;
        }
        else{
            return (int)ans;
        }
    }
};