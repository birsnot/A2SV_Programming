class Solution {
public:
    unordered_map<int, int> rep, sz;
    int find(int x){
        while (x != rep[x]){
            x = rep[x] = rep[rep[x]];
        }
        return x;
    }
    void merge(int x, int y){
        x = find(x);
        y = find(y);
        if (x == y) return;
        if(sz[x] < sz[y]) swap(x, y);
        rep[y] = x;
        sz[x] += sz[y];
    }
    int removeStones(vector<vector<int>>& stones) {
        unordered_map<int, vector<int>> cmnR;
        for(auto p: stones){
            cmnR[p[0]].push_back(p[1]);
            rep[p[1]] = p[1];
            sz[p[1]] = 1;
        }
        for(auto cmns: cmnR){
            int x = cmns.second[0];
            for(int i = 1; i < cmns.second.size(); ++i){
                merge(x, cmns.second[i]);
            }
        }
        int ans = 0;
        for(auto x: rep){
            if(x.first == x.second) ++ans;
        }
        return stones.size() - ans;
    }
};