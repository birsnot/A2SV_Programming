class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int l = 0, count = 0, ans = 0, odd_count = 0;
        for (auto n: nums){
            if(n%2){
                ++odd_count;
                count = 0;
            }
            while(odd_count == k){
                if(nums[l]%2){
                    --odd_count;
                }
                ++count;
                ++l;
            }
            ans += count;
        }
        return ans;
    }
};