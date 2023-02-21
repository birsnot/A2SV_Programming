class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int N = nums.size() - 1;
        int left = 0;
        int right = N/2;
        int mid = left + right;
        while (left < right){
            mid += 1 - mid%2;
            if(nums[mid] == nums[mid-1]){
                    left = mid/2 + 1;
            }
            else{
                right = mid/2;
            }
            mid = left + right;
        }
        return nums[left*2];
    }
};