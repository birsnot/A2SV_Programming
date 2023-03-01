class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
         vector<int> vals(k,0);
        vals[0] = 1;
        int total = 0;


        for(auto j:nums)
        {
               total = total + (j%k + k)%k;

              vals[total%k]++;

        }

        int res = 0;
        for(auto m:vals)
        {
              res = res + (m*(m-1))/2;
        }

        return res;
    }
};