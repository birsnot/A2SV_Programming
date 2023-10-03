class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(), costs.end(), [&](vector<int> &a, vector<int> &b){
            return abs(a[0] - a[1]) > abs(b[0] - b[1]);
        });
        int a = 0, b = 0, N = costs.size()/2, total = 0;
        for(auto &cost: costs){
            if((a < N && cost[0] < cost[1]) || b == N){
                a++;
                total += cost[0];
            }
            else {
                b++;
                total += cost[1];
            }
        }
        return total;
    }
};