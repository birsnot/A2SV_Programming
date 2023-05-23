class Solution {
public:
    vector<int> rep, sz;
    Solution(): rep(26), sz(26, 1){
        iota(rep.begin(), rep.end(), 0);
    }
    int find(int x){
        while(x != rep[x]){
            x = rep[x] = rep[rep[x]];
        }
        return x;
    }

    bool equationsPossible(vector<string>& equations) {
        int x, y;
        for(auto eq: equations){
            if(eq[1] == '='){
                x = find(eq[0] - 'a');
                y = find(eq[3] - 'a');
                if (x == y) continue;
                if (sz[x] < sz[y]) swap(x, y);
                rep[y] = x;
                sz[x] += sz[y];
            }
        }
        for(auto eq: equations){
            if(eq[1] == '!' && (find(eq[0] - 'a') == find(eq[3] - 'a'))) return false;
        }
        return true;
    }
};