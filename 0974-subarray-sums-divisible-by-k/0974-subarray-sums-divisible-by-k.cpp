class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector <int> sofar(k);
        sofar[0] = 1;
        long sum_ = 0, ans = 0, mod;
        for(auto n: nums){
            sum_ += n;
            mod = (sum_%k + k)%k;
            ans += sofar[mod]++;
        }
        return ans;
    }
};