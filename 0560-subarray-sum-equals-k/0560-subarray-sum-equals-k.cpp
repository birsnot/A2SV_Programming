class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> match;
        match[0] = 1;
        int ans = 0;
        long sum_ = 0;
        for(auto n: nums){
            sum_ += n;
            ans += match[sum_ - k];
            ++match[sum_];
        }
        return ans;
    }
};