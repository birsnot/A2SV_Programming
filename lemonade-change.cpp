class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fives = 0, tens = 0;
        for(auto bill: bills){
            if(bill == 5) ++fives;
            else if(bill == 10){
                if(fives-- == 0) return false;
                ++tens;
            }
            else {
                if(fives-- == 0) return false;
                if(tens) --tens;
                else if(fives < 2) return false;
                else fives -= 2;
            }
        }
        return true;
    }
};