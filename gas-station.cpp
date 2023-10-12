class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int N = gas.size();
        int peak = -1, valley = 0, prev_n = 0, cur = 0;
        for(int i = 0; i < N; ++i){
            cur += gas[i] - cost[i];
            if(cur >= prev_n && peak == -1){
                peak = i;
                valley = prev_n;
            }
            else if(cur < valley){
                peak = -1;
            }
            prev_n = cur;
        }
        return cur >= 0 ? peak : -1;
    }
};