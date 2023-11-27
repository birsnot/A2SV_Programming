int cnt[101];

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        memset(cnt, 0, sizeof cnt);
        int ans = 0;
        for(auto n: nums){
            ans += cnt[n];
            cnt[n]++;
        }
        return ans;
    }
};