class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector <int> path(1001);
        for(auto &trip: trips){
            path[trip[1]] += trip[0];
            path[trip[2]] -= trip[0];
        }
        int sum_ = 0;
        for(auto n: path){
            sum_ += n;
            if (sum_ > capacity){
                return false;
            }
        }
        return true;
    }
};