class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prev;
        int N = nums.size();
        for(int i = 0; i < N; ++i){
            if(prev.count(target - nums[i])){
                return {prev[target - nums[i]], i};
            }
            prev[nums[i]] = i;
        }
        return {-1, -1};
    }
};