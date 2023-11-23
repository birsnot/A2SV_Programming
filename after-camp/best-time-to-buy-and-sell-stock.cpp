class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_ = INT_MAX, ans = INT_MIN;
        for(auto p: prices){
            ans = max(ans, p - min_);
            min_ = min(p, min_);
        }
        return max(0, ans);
    }
};