class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> match;
        match[0] = 1;
        int ans = 0;
        long sum_ = 0;
        int check;
        for(auto n: nums){
            sum_ += n;
            check = sum_ - k;
            if(match.find(check) != match.end()){
                ans += match[check];
            }
            ++match[sum_];
        }
        return ans;
    }
};