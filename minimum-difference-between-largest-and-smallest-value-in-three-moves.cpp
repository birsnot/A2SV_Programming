class Solution {
public:
    int minDifference(vector<int>& nums) {
        int N = nums.size();
        if(N < 5) return 0;
        int last = N - 4, l = 0, r = N - 1;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < 3; ++i){
            if(nums[l + last] - nums[l] < nums[r] - nums[r - last]){
                r -= 1;
            }
            else{
                l += 1;
            }
        }
        return nums[l + last] - nums[l];
    }
};