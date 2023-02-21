class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int N = nums.size() - 1;
        int left = 0;
        int right = N/2;
        int mid = left + right;
        while (mid < N){
            mid -= mid%2;
            if(nums[mid] != nums[mid+1]){
                if(mid == 0 || nums[mid] != nums[mid-1]){
                    return nums[mid];
                }
                else{
                    right = mid/2 - 1;
                }
            }
            else{
                left = mid/2 + 1;
            }
            mid = left + right;
        }
        return nums[N];
    }
};