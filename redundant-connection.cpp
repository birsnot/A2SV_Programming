class Solution {
public:
    vector<int> rep, sz;
    int find(int x){
        while(x != rep[x]){
            x = rep[x] = rep[rep[x]];
        }
        return x;
    }
    bool merge(int x, int y){
        x = find(x);
        y = find(y);
        if(x == y) return false;
        if(sz[x] < sz[y]) swap(x, y);
        rep[y] = x;
        sz[x] += sz[y];
        return true;
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        rep.resize(n);
        iota(rep.begin(), rep.end(), 0);
        sz.assign(n, 1);
        for(auto& e: edges) if(!merge(e[0], e[1])) return e;
        return {0, 0};
    }
};