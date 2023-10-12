class Solution {
public:
    int maxSubarrays(vector<int>& nums) {
        const int ONES = (1<<21) - 1;
        int cnt = 0, cur = ONES;
        for(auto n: nums){
            cur &= n;
            if(!cur){
                cnt++;
                cur = ONES;
            }
        }
        return max(cnt, 1);
    }
};