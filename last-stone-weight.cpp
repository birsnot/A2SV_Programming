class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(), stones.end());
        int x, y;
        while(stones.size() > 1){
            y = stones[0]; 
            pop_heap(stones.begin(), stones.end()); stones.pop_back();
            x = stones[0];
            pop_heap(stones.begin(), stones.end()); stones.pop_back();
            if (x == y) continue;
            stones.push_back(y - x);
            push_heap(stones.begin(), stones.end());
        }
        if(stones.empty()) return 0;
        return stones[0];
    }
};