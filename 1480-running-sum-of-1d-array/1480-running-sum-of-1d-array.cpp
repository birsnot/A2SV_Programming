class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> pre;
        long sum_ = 0;
        for(int i = 0; i < nums.size(); ++i){
            sum_ += nums[i];
            pre.push_back(sum_);
        }
        return pre;
    }
};