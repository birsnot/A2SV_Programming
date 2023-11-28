class Solution {
public:
    int compare(int a, int b){
        if (a == b) return 0;
        return a > b ? 1 : -1;
    }
    bool isMonotonic(vector<int>& nums) {
        int _slope = -1*compare(nums[0], nums[nums.size() - 1]);
        if(_slope == 0) _slope = 1;
        for(int i = 1; i < nums.size(); ++i){
            if(compare(nums[i - 1], nums[i]) == _slope) return false;
        }
        return true;
    }
};