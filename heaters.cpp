class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(heaters.begin(), heaters.end());
        sort(houses.begin(), houses.end());
        int N = houses.size(), M = heaters.size();

        int prev_heater = INT_MIN/2, i = 0, ans = houses[N - 1] - heaters[M - 1];
        for(auto heater: heaters){
            while(i < N && houses[i] <= heater){
                int prev_dis = houses[i] - prev_heater;
                int cur_dis = heater - houses[i];
                ans = max(ans, min(prev_dis, cur_dis));
                i++;
            }
            prev_heater = heater;
        }
        return ans;
    }
};