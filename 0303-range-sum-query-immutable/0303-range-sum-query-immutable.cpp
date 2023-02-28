class NumArray {
public:
    vector <int> nums_;
    NumArray(vector<int>& nums) {
        nums_.push_back(0);
        long sum_ = 0;
        for (auto n: nums){
            sum_ += n;
            nums_.push_back(sum_);
        }
    }
    
    int sumRange(int left, int right) {
        return nums_[right + 1] - nums_[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */