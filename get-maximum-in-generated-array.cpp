class Solution {
public:
    int getMaximumGenerated(int n) {
        if(n < 2) return n;
        int nums[n + 1];
        nums[0] = 0; nums[1] = 1;
        for(int i = 2; i <= n; ++i){
            nums[i] = nums[i/2] + (i%2)*nums[i/2 + 1];
        }
        return *max_element(nums, nums + n + 1);
    }
};