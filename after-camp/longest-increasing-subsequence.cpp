class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> lis;
        for(auto n: nums){
            if(lis.empty() || lis.back() < n) lis.push_back(n);
            else{
                *lower_bound(lis.begin(), lis.end(), n) = n;
            }
        }
        return lis.size();
    }
};