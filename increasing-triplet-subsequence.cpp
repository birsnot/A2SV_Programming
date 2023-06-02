class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX, second = INT_MAX;
        for(auto n: nums){
            if(n <= second){
                if(n > first){
                    second = n;
                }
                else{
                    first = n;
                }
            }
            else return true;
        }
        return false;
    }
};