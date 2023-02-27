class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> my_fruits;
        int l = 0;
        for(auto fr: fruits){
            my_fruits[fr] += 1;
            if (my_fruits.size() > 2){
                if(my_fruits[fruits[l]] == 1){
                    my_fruits.erase(fruits[l]);
                }
                else{
                    --my_fruits[fruits[l]];
                }
                ++l;
            }
        }
        return fruits.size() - l;
    }
};