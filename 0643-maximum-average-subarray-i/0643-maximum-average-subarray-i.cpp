class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        long double sum_;
        int N = k;
        if (nums.size() < k) N = nums.size();
        int i = 0;
        for (; i < N; ++i){
            sum_ += nums[i];
        }
        long double maxSum = sum_;
        int l = 0;
        for (; i < nums.size(); ++i, ++l){
            sum_ += nums[i] - nums[l];
            if (sum_ > maxSum) maxSum = sum_;
        }
        return (double)(maxSum/k);
    }
};