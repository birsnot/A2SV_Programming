class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int N = nums.size();
        vector<int> mins(N);
        mins[0] = nums[0];
        for(int i = 1; i < N; ++i) mins[i] = min(mins[i - 1], nums[i]);
        stack<int> monoStk; monoStk.push(INT_MAX);
        for(int i = N - 1; i >= 0; --i){
            while(mins[i] >= monoStk.top()) monoStk.pop();
            if(nums[i] > monoStk.top() && monoStk.top() > mins[i]) return true;
            if(monoStk.top() > nums[i]) monoStk.push(nums[i]);
        }
        return false;
    }
};