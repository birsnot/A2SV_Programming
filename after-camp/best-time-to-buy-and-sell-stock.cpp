class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_ = INT_MAX, ans = 0;
        for(auto price: prices){
            ans = max(ans, price - min_);
            min_ = min(min_, price);
        }
        return ans;
    }
};