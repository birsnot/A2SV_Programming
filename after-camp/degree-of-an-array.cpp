class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, array<int, 3>> win;
        int N = nums.size();
        for(int i = 0; i < N; ++i){
            if(win.count(nums[i])){
                win[nums[i]][0]++;
                win[nums[i]][2] = i;
            }
            else win[nums[i]] = {1, i, i};
        }
        int max_fq = 0, ans = N;
        for(auto &[_, val]: win){
            auto [fq, st, end] = val;
            if(fq > max_fq){
                max_fq = fq;
                ans = end - st;
            }
            else if(fq == max_fq) ans = min(ans, end - st);
        }
        return ans + 1;
    }
};