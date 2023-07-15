class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int max_ = INT_MIN;
        int left = values[0] - 1;
        for(int i = 1; i < values.size(); ++i){
            max_ = max(max_, left + values[i]);
            left = max(left, values[i]) - 1;
        }
        return max_;
    }
};