class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if(prices.size() == 1) return 0;
        int buy = 0, sell = -prices[0] - fee;
        for(int i = 1; i < prices.size(); ++i){
            int cur_sell = max(sell, buy - prices[i] - fee);
            buy = max(buy, sell + prices[i]);
            sell = cur_sell;
        }
        return max(buy, sell);
    }
};